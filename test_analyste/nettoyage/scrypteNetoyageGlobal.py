# ============================================================
# Nettoyage et Préparation des Données
# Objectif : Produire un dataset propre, cohérent et exploitable
# Auteur : Steph ADZO
# ============================================================

import pandas as pd
import numpy as np
import os

# -----------------------------
# 1. Chargement des fichiers
# -----------------------------

root_dir = os.path.join('..', os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(root_dir, 'data')
raw_data_dir = os.path.join(data_dir, 'brutes')
clean_data_dir = os.path.join(data_dir, 'nettoyees')
files = {
    "centres_service": os.path.join(raw_data_dir, "centres_service.csv"),
    "demandes_service_public": os.path.join(raw_data_dir, "demandes_service_public.csv"),
    "details_communes": os.path.join(raw_data_dir, "details_communes.csv"),
    "developpement": os.path.join(raw_data_dir, "developpement.csv"),
    "documents_administratifs": os.path.join(raw_data_dir, "documents_administratifs_ext.csv"),
    "donnees_socioeconomiques": os.path.join(raw_data_dir, "donnees_socioeconomiques.csv"),
    "logs_activite": os.path.join(raw_data_dir, "logs_activite.csv"),
    "reseau_routier": os.path.join(raw_data_dir, "reseau_routier_togo_ext.csv")
}

dfs = {name: pd.read_csv(path) for name, path in files.items()}

# -----------------------------
# 2. Nettoyage général
# -----------------------------

for name, df in dfs.items():
    print(f"\n--- Nettoyage pour : {name} ---")
    
    # 2.1 Suppression des doublons
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    after = df.shape[0]
    print(f"Doublons supprimés : {before - after}")
    
    # 2.2 Gestion des valeurs manquantes
    na_counts = df.isnull().sum()
    print("Valeurs manquantes :")
    print(na_counts[na_counts > 0])
    
    # 2.3 Harmonisation des types
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')  # Conversion en datetime
        elif df[col].dtype == object:
            df[col] = df[col].str.strip()  # Suppression des espaces
            df[col] = df[col].replace({'N/A': np.nan, 'n/a': np.nan})  # Normalisation NA
    dfs[name] = df

# -----------------------------
# 3. Traitements spécifiques par fichier
# -----------------------------

# 3.1 centres_service
df = dfs['centres_service']
# Vérification des capacités négatives ou aberrantes
df['personnel_capacite_jour'] = df['personnel_capacite_jour'].apply(lambda x: np.nan if x < 0 else x)
# Remplacement NA par la moyenne par type_centre
df['personnel_capacite_jour'] = df.groupby('type_centre')['personnel_capacite_jour'].transform(lambda x: x.fillna(x.mean()))
dfs['centres_service'] = df

# 3.2 demandes_service_public
df = dfs['demandes_service_public']
# Remplacement des valeurs manquantes pour type_document ou statut par "Inconnu"
df['type_document'] = df['type_document'].fillna('Inconnu')
df['statut_demande'] = df['statut_demande'].fillna('Inconnu')
# Correction des délais aberrants (<0)
df['delai_traitement_jours'] = df['delai_traitement_jours'].apply(lambda x: np.nan if x < 0 else x)
# Remplacement NA par la médiane
df['delai_traitement_jours'] = df['delai_traitement_jours'].fillna(df['delai_traitement_jours'].median())
dfs['demandes_service_public'] = df

# 3.3 logs_activite
df = dfs['logs_activite']
# Nombre de documents négatif → remplacer par NA
df['nombre_traite'] = df['nombre_traite'].apply(lambda x: np.nan if x < 0 else x)
df['nombre_rejete'] = df['nombre_rejete'].apply(lambda x: np.nan if x < 0 else x)
# Remplir raison_rejet manquante par "Pas de rejet"
df['raison_rejet'] = df['raison_rejet'].fillna('Pas de rejet')
dfs['logs_activite'] = df

# 3.4 documents_administratifs
df = dfs['documents_administratifs']
df['nombre_demandes'] = df['nombre_demandes'].apply(lambda x: np.nan if x < 0 else x)
df['delai_moyen_jours'] = df['delai_moyen_jours'].apply(lambda x: np.nan if x < 0 else x)
df['taux_rejet_moyen'] = df['taux_rejet_moyen'].apply(lambda x: np.nan if x < 0 else x)
dfs['documents_administratifs'] = df

# 3.5 Harmonisation des noms de colonnes (exemple)
for name, df in dfs.items():
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    dfs[name] = df

# -----------------------------
# 4. Export des datasets nettoyés
# -----------------------------
for name, df in dfs.items():
    df.to_csv(os.path.join(clean_data_dir, f"cleaned_{name}.csv"), index=False)
    print(f"Dataset nettoyé exporté : cleaned_{name}.csv")

# -----------------------------
# 5. Documentation synthétique des choix
# -----------------------------
print("\n=== Documentation des transformations ===")
print("""
1. Suppression des doublons sur tous les fichiers.
2. Conversion des colonnes date en format datetime.
3. Nettoyage des chaînes de caractères (trim, remplacement N/A par NaN).
4. Valeurs numériques aberrantes (négatives) remplacées par NaN.
5. Remplissage des valeurs manquantes :
   - Par la moyenne ou médiane pour les variables numériques (ex: capacite_jour, delai_traitement_jours)
   - Par "Inconnu" ou "Pas de rejet" pour les variables catégorielles.
6. Harmonisation des noms de colonnes (minuscules, underscores).
7. Export de datasets nettoyés pour analyses ultérieures.
""")
