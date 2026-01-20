# edaDonneesSocioEconomiques.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Chargement des données ---
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'donnees_socioeconomiques.csv')
df = pd.read_csv(file_path)

# --- Aperçu des données ---
print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions :", df.shape)

# --- Informations générales ---
print("\nInformations générales :")
print(df.info())

# --- Statistiques descriptives numériques ---
print("\n=== Statistiques descriptives numériques ===")
print(df.describe())

# --- Qualité des données ---
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# --- Répartition des régions ---
print("\n=== Répartition des régions ===")
print(df['region'].value_counts())

# --- Visualisations ---
sns.set(style="whitegrid")

# Histogrammes pour variables numériques
num_cols = ['population','superficie_km2','densite','taux_urbanisation',
            'taux_alphabétisation','age_median','nombre_menages','revenu_moyen_fcfa']

df[num_cols].hist(figsize=(15,10), bins=15, edgecolor='black')
plt.suptitle("Distribution des variables socio-économiques", fontsize=16)
plt.show()

# Boxplot pour comparer les revenus moyens par région
plt.figure(figsize=(10,6))
sns.boxplot(x='region', y='revenu_moyen_fcfa', data=df)
plt.title("Revenu moyen par région")
plt.ylabel("Revenu moyen (FCFA)")
plt.show()

# Scatter plot : densité vs revenu moyen
plt.figure(figsize=(8,6))
sns.scatterplot(x='densite', y='revenu_moyen_fcfa', hue='region', data=df, s=100)
plt.title("Densité vs Revenu moyen par commune")
plt.xlabel("Densité (habitants/km²)")
plt.ylabel("Revenu moyen (FCFA)")
plt.legend(title='Région')
plt.show()

# Corrélation entre variables numériques
plt.figure(figsize=(10,8))
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()
