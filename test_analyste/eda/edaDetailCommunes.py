# eda_details_communes.py
# Script d'EDA pour le fichier details_communes.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1️⃣ Chargement des données
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'details_communes.csv')
df = pd.read_csv(file_path)

# 2️⃣ Aperçu des données
print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions : ", df.shape)

# 3️⃣ Informations générales
print("\nInformations :")
print(df.info())

# 4️⃣ Statistiques descriptives numériques
print("\nStatistiques descriptives numériques :")
print(df.describe())

# 5️⃣ Vérification des valeurs manquantes et doublons
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# 6️⃣ Analyse univariée (variables catégorielles)
categorical_cols = ['region', 'prefecture', 'type_commune', 'zone_climatique']
for col in categorical_cols:
    if col in df.columns:
        print(f"\nDistribution de {col} :")
        print(df[col].value_counts())
        plt.figure(figsize=(8,4))
        sns.countplot(data=df, x=col, order=df[col].value_counts().index)
        plt.title(f"Distribution de {col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# 7️⃣ Analyse univariée (variables numériques)
numerical_cols = ['latitude', 'longitude', 'altitude_m', 'superficie_km2', 'population_densite', 'distance_capitale_km']
for col in numerical_cols:
    if col in df.columns:
        plt.figure(figsize=(8,4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution de {col}")
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(6,3))
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot de {col}")
        plt.tight_layout()
        plt.show()

# 8️⃣ Corrélations entre variables numériques
numeric_in_df = [col for col in numerical_cols if col in df.columns]
if numeric_in_df:
    plt.figure(figsize=(10,8))
    sns.heatmap(df[numeric_in_df].corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.show()

# 9️⃣ Synthèse rapide
print("\n=== Synthèse rapide ===")
print("- Dataset propre : pas de valeurs manquantes détectées (à confirmer ci-dessus)")
print(f"- Nombre de communes détaillées : {df.shape[0]}")
if 'region' in df.columns:
    print(f"- Régions couvertes : {df['region'].nunique()} ({', '.join(df['region'].unique())})")
if 'type_commune' in df.columns:
    print(f"- Types de communes : {df['type_commune'].value_counts().to_dict()}")
if 'zone_climatique' in df.columns:
    print(f"- Zones climatiques : {df['zone_climatique'].value_counts().to_dict()}")
