# ============================================================
# Analyse Exploratoire des Données (EDA)
# Dataset : Centres administratifs
# Objectif : Comprendre la structure, la qualité et les tendances des données
# Auteur : Steph ADZO
# ============================================================

# -----------------------------
# 1. Import des librairies
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# 2. Chargement des données
# -----------------------------
# Le fichier CSV doit être dans le même dossier que ce script
df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'centres_service.csv'))
# Aperçu des premières lignes
print("Aperçu des données :")
print(df.head())

# -----------------------------
# 3. Dimensions et structure
# -----------------------------
print("\nDimensions du dataset (lignes, colonnes) :")
print(df.shape)

print("\nInformations générales :")
print(df.info())

# -----------------------------
# 4. Statistiques descriptives
# -----------------------------
print("\nStatistiques descriptives des variables numériques :")
print(df.describe())

# -----------------------------
# 5. Qualité des données
# -----------------------------

# Valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())

# Doublons
print("\nNombre de lignes dupliquées :")
print(df.duplicated().sum())

# -----------------------------
# 6. Analyse univariée
# -----------------------------

# Répartition des types de centres
print("\nRépartition des types de centres :")
print(df["type_centre"].value_counts())

# Histogramme de la capacité journalière
plt.figure()
plt.hist(df["personnel_capacite_jour"], bins=20)
plt.title("Distribution de la capacité journalière")
plt.xlabel("Capacité par jour")
plt.ylabel("Nombre de centres")
plt.show()

# -----------------------------
# 7. Analyse bivariée
# -----------------------------

# Capacité moyenne par type de centre
capacite_par_type = df.groupby("type_centre")["personnel_capacite_jour"].mean()
print("\nCapacité moyenne par type de centre :")
print(capacite_par_type)

# Boxplot capacité vs type de centre
plt.figure()
df.boxplot(column="personnel_capacite_jour", by="type_centre")
plt.title("Capacité journalière selon le type de centre")
plt.suptitle("")  # Supprime le titre automatique
plt.xlabel("Type de centre")
plt.ylabel("Capacité journalière")
plt.show()

# -----------------------------
# 8. Analyse par région
# -----------------------------

print("\nNombre de centres par région :")
print(df["region"].value_counts())

# -----------------------------
# 9. Équipement numérique
# -----------------------------

print("\nRépartition de l'équipement numérique :")
print(df["equipement_numerique"].value_counts())

capacite_par_equipement = df.groupby("equipement_numerique")["personnel_capacite_jour"].mean()
print("\nCapacité moyenne selon l'équipement numérique :")
print(capacite_par_equipement)

# -----------------------------
# 10. Insights finaux
# -----------------------------
print("\nINSIGHTS PRINCIPAUX :")
print("- Les centres secondaires sont majoritaires")
print("- Les centres principaux ont une capacité journalière nettement plus élevée")
print("- Un équipement numérique complet est associé à une meilleure capacité")
print("- Certaines régions concentrent peu de centres à forte capacité")

# ============================================================
# Fin du script EDA
# ============================================================
