# -*- coding: utf-8 -*-
"""
EDA pour le réseau routier du Togo
Auteur : Steph ADZO
"""

# -------------------------
# 1. Import des librairies
# -------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration esthétique des graphiques
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# -------------------------
# 2. Chargement des données
# -------------------------
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'reseau_routier_togo_ext.csv')
df = pd.read_csv(file_path)

# -------------------------
# 3. Aperçu et structure
# -------------------------
print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions :", df.shape)
print("\nInformations générales :")
print(df.info())

# -------------------------
# 4. Statistiques descriptives
# -------------------------
print("\n=== Statistiques descriptives numériques ===")
print(df.describe())

# -------------------------
# 5. Qualité des données
# -------------------------
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :\n", df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# -------------------------
# 6. Répartition des routes par type
# -------------------------
print("\n=== Répartition des routes par type ===")
print(df['type_route'].value_counts())

# Visualisation
sns.countplot(x='type_route', data=df, palette='Set2')
plt.title("Nombre de routes par type")
plt.show()

# -------------------------
# 7. État des routes
# -------------------------
print("\n=== État des routes ===")
print(df['etat_route'].value_counts())

sns.countplot(x='etat_route', data=df, palette='Set1', order=['Bon','Moyen','Mediocre'])
plt.title("État des routes")
plt.show()

# -------------------------
# 8. Longueur des routes
# -------------------------
print("\n=== Longueur des routes ===")
print(df['longueur_km'].describe())

sns.histplot(df['longueur_km'], bins=15, kde=True, color='skyblue')
plt.title("Distribution des longueurs de routes (km)")
plt.xlabel("Longueur (km)")
plt.ylabel("Nombre de routes")
plt.show()

# -------------------------
# 9. Temps de parcours
# -------------------------
print("\n=== Temps de parcours par route ===")
print(df['temps_parcours_heures'].describe())

sns.boxplot(x='type_route', y='temps_parcours_heures', data=df, palette='Set3')
plt.title("Temps de parcours moyen par type de route")
plt.ylabel("Temps (heures)")
plt.show()

# -------------------------
# 10. Flux de véhicules
# -------------------------
sns.scatterplot(x='bus_par_jour', y='camions_par_jour', hue='etat_route', data=df, palette='Set1', s=100)
plt.title("Relation Bus vs Camions par jour selon l'état des routes")
plt.xlabel("Bus par jour")
plt.ylabel("Camions par jour")
plt.show()

sns.histplot(df['passagers_par_jour'], bins=20, color='orange')
plt.title("Distribution du nombre de passagers par jour")
plt.xlabel("Passagers par jour")
plt.ylabel("Nombre de routes")
plt.show()

# -------------------------
# 11. Corrélations numériques
# -------------------------
print("\n=== Matrice de corrélation ===")
corr = df[['longueur_km','temps_parcours_heures','points_controle','bus_par_jour','camions_par_jour','passagers_par_jour']].corr()
print(corr)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Corrélations entre variables numériques")
plt.show()

# -------------------------
# 12. Synthèse des constats
# -------------------------
print("\n=== Synthèse ===")
print("- Le réseau routier se compose principalement de routes nationales, régionales et locales.")
print("- L'état des routes varie : certaines sont en bon état, d'autres moyens ou médiocres, impactant le temps de parcours.")
print("- Les routes plus longues ont souvent un temps de parcours plus élevé et plus de points de contrôle.")
print("- Le trafic est concentré sur certaines routes : les bus, camions et passagers sont inégalement répartis.")
print("- Les routes en mauvais état semblent concentrer moins de passagers et plus de temps de parcours.")

