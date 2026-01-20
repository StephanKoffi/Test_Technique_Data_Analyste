# ============================================================
# Analyse Exploratoire des Données (EDA) - Demandes Service Public
# Objectif : Comprendre la structure, la qualité et la distribution des données
# Auteur : Steph ADZO
# ============================================================

# -----------------------------
# 1. Import des librairies
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# -----------------------------
# 2. Chargement des données
# -----------------------------
df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'demandes_service_public.csv'))

# -----------------------------
# 3. Aperçu des données
# -----------------------------
print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions : ", df.shape)
print("\nInformations :")
print(df.info())
print("\nStatistiques descriptives numériques :")
print(df.describe())

# -----------------------------
# 4. Qualité des données
# -----------------------------
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# -----------------------------
# 5. Conversion des dates
# -----------------------------
if 'date_demande' in df.columns:
    df['date_demande'] = pd.to_datetime(df['date_demande'], errors='coerce')

# -----------------------------
# 6. Analyse univariée
# -----------------------------
print("\n=== Analyse univariée ===")

# Type de document
if 'type_document' in df.columns:
    print("Répartition des types de documents :")
    print(df['type_document'].value_counts())
    sns.countplot(data=df, x='type_document')
    plt.title("Répartition des types de documents")
    plt.xticks(rotation=45)
    plt.show()

# Statut des demandes
if 'statut_demande' in df.columns:
    print("Répartition du statut des demandes :")
    print(df['statut_demande'].value_counts())
    sns.countplot(data=df, x='statut_demande')
    plt.title("Répartition du statut des demandes")
    plt.xticks(rotation=45)
    plt.show()

# Analyse des montants ou valeurs numériques (si existants)
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
for col in numeric_cols:
    plt.figure(figsize=(8,4))
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(f"Distribution de {col}")
    plt.show()

# -----------------------------
# 7. Analyse bivariée
# -----------------------------
# Exemple : statut par type de document
if 'type_document' in df.columns and 'statut_demande' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(x='type_document', hue='statut_demande', data=df)
    plt.title("Statut des demandes par type de document")
    plt.xticks(rotation=45)
    plt.show()

# Exemple : age vs statut
if 'age' in df.columns and 'statut_demande' in df.columns:
    plt.figure(figsize=(8,4))
    sns.boxplot(x='statut_demande', y='age', data=df)
    plt.title("Âge des demandeurs selon le statut de la demande")
    plt.show()

# -----------------------------
# 8. Analyse temporelle
# -----------------------------
if 'date_demande' in df.columns:
    df['annee_demande'] = df['date_demande'].dt.year
    plt.figure(figsize=(8,4))
    sns.countplot(x='annee_demande', data=df, palette='viridis')
    plt.xticks(rotation=45)
    plt.title("Nombre de demandes par année")
    plt.show()

# -----------------------------
# 9. Détection des valeurs aberrantes
# -----------------------------
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[col] < (q1 - 1.5*iqr)) | (df[col] > (q3 + 1.5*iqr))]
    if not outliers.empty:
        print(f"\nValeurs aberrantes détectées dans {col} :")
        print(outliers[[col]])

# -----------------------------
# 10. Synthèse automatique
# -----------------------------
print("\n=== Synthèse des principaux constats ===")
print(f"- Dataset : {df.shape[0]} demandes, {df.shape[1]} colonnes")
print("- Vérifier les doublons et les valeurs manquantes :", df.duplicated().sum(), "doublons, valeurs manquantes :")
print(df.isnull().sum().to_dict())

if 'type_document' in df.columns:
    print(f"- Répartition des types de documents : {df['type_document'].value_counts().to_dict()}")
if 'statut_demande' in df.columns:
    print(f"- Répartition des statuts des demandes : {df['statut_demande'].value_counts().to_dict()}")

if 'age' in df.columns:
    print(f"- Âge moyen des demandeurs : {df['age'].mean():.2f} ans")

print("- Analyse des variables numériques et distribution des valeurs aberrantes effectuée")
print("- Analyse temporelle réalisée sur les années des demandes si disponibles")
