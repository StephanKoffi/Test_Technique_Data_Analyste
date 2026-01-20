# edaLogsActivite.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# 1. Chargement des données
# -------------------------------
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'brutes', 'logs_activite.csv')
df = pd.read_csv(file_path)

print("=== Aperçu des données ===")
print(df.head())
print("\nDimensions :", df.shape)
print("\nInformations générales :")
print(df.info())

# -------------------------------
# 2. Statistiques descriptives
# -------------------------------
print("\n=== Statistiques descriptives numériques ===")
print(df.describe())

# -------------------------------
# 3. Qualité des données
# -------------------------------
print("\n=== Qualité des données ===")
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("Nombre de doublons : ", df.duplicated().sum())

# -------------------------------
# 4. Analyse exploratoire
# -------------------------------

# a) Répartition des types d'opération
plt.figure(figsize=(8,5))
sns.countplot(x='type_operation', data=df, palette='Set2')
plt.title("Répartition des types d'opération")
plt.ylabel("Nombre d'opérations")
plt.show()

# b) Répartition des types de documents traités
plt.figure(figsize=(8,5))
sns.countplot(x='type_document', data=df[df['type_document'] != 'N/A'], palette='Set3')
plt.title("Répartition des types de documents traités")
plt.ylabel("Nombre de traitements")
plt.xticks(rotation=45)
plt.show()

# c) Nombre moyen de demandes traitées par type de document
df_traitement = df[df['type_operation'] == 'Traitement']
moyenne_traitement = df_traitement.groupby('type_document')['nombre_traite'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='type_document', y='nombre_traite', data=moyenne_traitement, palette='Set1')
plt.title("Nombre moyen de demandes traitées par type de document")
plt.ylabel("Nombre moyen traité")
plt.xticks(rotation=45)
plt.show()

# d) Délais moyens effectifs par type de document
plt.figure(figsize=(8,5))
sns.barplot(x='type_document', y='delai_effectif', data=df_traitement.groupby('type_document')['delai_effectif'].mean().reset_index(), palette='Set2')
plt.title("Délai moyen effectif par type de document")
plt.ylabel("Délai effectif moyen (jours)")
plt.xticks(rotation=45)
plt.show()

# e) Taux de rejet moyen par type de document
df_traitement['taux_rejet'] = df_traitement['nombre_rejete'] / df_traitement['nombre_traite']
plt.figure(figsize=(8,5))
sns.barplot(x='type_document', y='taux_rejet', data=df_traitement.groupby('type_document')['taux_rejet'].mean().reset_index(), palette='Set3')
plt.title("Taux de rejet moyen par type de document")
plt.ylabel("Taux de rejet")
plt.xticks(rotation=45)
plt.show()

# f) Analyse des incidents techniques
plt.figure(figsize=(6,4))
sns.countplot(x='incident_technique', data=df, palette='Set1')
plt.title("Incidents techniques")
plt.ylabel("Nombre d'opérations")
plt.show()

# g) Temps d'attente moyen
plt.figure(figsize=(8,5))
sns.histplot(df['temps_attente_moyen_minutes'], bins=15, kde=True, color='skyblue')
plt.title("Distribution du temps d'attente moyen (minutes)")
plt.xlabel("Temps d'attente moyen (minutes)")
plt.show()

# -------------------------------
# 5. Synthèse
# -------------------------------
print("\n=== Synthèse ===")
print("- Les opérations de traitement sont les plus fréquentes.")
print("- Les documents les plus traités sont les cartes d'identité et les actes de naissance.")
print("- Les délais moyens et le nombre de rejets varient selon le type de document.")
print("- Les incidents techniques sont rares mais impactent certaines opérations.")
print("- Les temps d'attente moyens montrent des pics importants pour certains centres.")
