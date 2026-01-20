# eda_developpement.py
# Script EDA pour le fichier developpement.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1️⃣ Chargement des données
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'developpement.csv')
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

# 6️⃣ Analyse univariée (catégorielles)
categorical_cols = ['region', 'prefecture', 'commune']
for col in categorical_cols:
    print(f"\nDistribution de {col} :")
    print(df[col].value_counts())
    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(f"Distribution de {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 7️⃣ Analyse univariée (numériques)
numerical_cols = [
    'pib_par_habitant_fcfa', 'taux_chomage', 'taux_pauvrete',
    'acces_electricite', 'acces_eau_potable', 'acces_internet',
    'indice_developpement', 'score_education', 'score_sante',
    'nombre_ecoles', 'nombre_hopitaux', 'nombre_banques'
]

for col in numerical_cols:
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

# 8️⃣ Corrélation entre variables numériques
plt.figure(figsize=(12,10))
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()

# 9️⃣ Synthèse rapide
print("\n=== Synthèse rapide ===")
print(f"- Dataset propre : {df.isnull().sum().sum()} valeurs manquantes")
print(f"- Nombre de communes : {df.shape[0]}")
print(f"- Régions couvertes : {df['region'].nunique()} ({', '.join(df['region'].unique())})")
print(f"- Nombre de préfectures : {df['prefecture'].nunique()}")
print(f"- Indicateurs principaux : PIB par habitant moyen = {df['pib_par_habitant_fcfa'].mean():,.0f} FCFA, taux de pauvreté moyen = {df['taux_pauvrete'].mean():.2f}")
