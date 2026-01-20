# edaDocumentsAdministratifs.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Charger le fichier CSV ---
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'documents_administratifs_ext.csv')
df = pd.read_csv(file_path)

# --- Aperçu des données ---
print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions :", df.shape)
print("\nInformations générales :")
print(df.info())

# --- Statistiques descriptives ---
print("\n=== Statistiques descriptives numériques ===")
print(df.describe())

# --- Qualité des données ---
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# --- Analyse univariée ---
print("\n=== Répartition des régions ===")
print(df['region'].value_counts())

print("\n=== Répartition des types de documents ===")
print(df['type_document'].value_counts())

# --- Visualisations exploratoires ---

# Histogramme du nombre de demandes
plt.figure(figsize=(8,5))
sns.histplot(df['nombre_demandes'], bins=20, kde=True, color='skyblue')
plt.title("Distribution du nombre de demandes")
plt.xlabel("Nombre de demandes")
plt.ylabel("Fréquence")
plt.show()

# Boxplot des délais moyens par type de document
plt.figure(figsize=(8,5))
sns.boxplot(x='type_document', y='delai_moyen_jours', data=df, palette='pastel')
plt.title("Délais moyens par type de document")
plt.xlabel("Type de document")
plt.ylabel("Délais moyens (jours)")
plt.xticks(rotation=45)
plt.show()

# Boxplot des taux de rejet moyens par type de document
plt.figure(figsize=(8,5))
sns.boxplot(x='type_document', y='taux_rejet_moyen', data=df, palette='muted')
plt.title("Taux de rejet moyen par type de document")
plt.xlabel("Type de document")
plt.ylabel("Taux de rejet moyen")
plt.xticks(rotation=45)
plt.show()

# Nombre de demandes par région
plt.figure(figsize=(8,5))
sns.barplot(x='region', y='nombre_demandes', data=df.groupby('region')['nombre_demandes'].sum().reset_index(), palette='Set2')
plt.title("Nombre total de demandes par région")
plt.xlabel("Région")
plt.ylabel("Nombre total de demandes")
plt.show()

# Moyenne des délais par région
plt.figure(figsize=(8,5))
sns.barplot(x='region', y='delai_moyen_jours', data=df.groupby('region')['delai_moyen_jours'].mean().reset_index(), palette='Set3')
plt.title("Délais moyens par région")
plt.xlabel("Région")
plt.ylabel("Délais moyens (jours)")
plt.show()

# Moyenne des taux de rejet par région
plt.figure(figsize=(8,5))
sns.barplot(x='region', y='taux_rejet_moyen', data=df.groupby('region')['taux_rejet_moyen'].mean().reset_index(), palette='coolwarm')
plt.title("Taux de rejet moyen par région")
plt.xlabel("Région")
plt.ylabel("Taux de rejet moyen")
plt.show()

# --- Synthèse écrite ---
print("\n=== Synthèse des principaux constats ===")
print("1. Les types de documents les plus demandés sont : Carte d'identité et Passeport.")
print("2. Les régions Maritime et Plateaux concentrent le plus grand nombre de demandes.")
print("3. Les délais moyens sont plus élevés pour les Passeports, tandis que les Cartes d'identité et Actes de naissance sont traités plus rapidement.")
print("4. Les taux de rejet sont globalement faibles, mais les Passeports présentent les valeurs les plus élevées.")
print("5. Les variations de délais et de taux de rejet montrent des disparités selon les régions et le type de document.")
