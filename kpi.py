import pandas as pd

# 1️⃣ Créer la liste de dictionnaires avec tes KPI
kpis = [
    {
        "Nom du KPI": "KPI 1 : Délai moyen de traitement",
        "Objectif métier": "Mesurer la performance opérationnelle",
        "Description / Interprétation": "Permet d’évaluer le temps moyen nécessaire pour traiter une demande dans un centre",
        "Règle de calcul": "Moyenne du delai_effectif pour toutes les demandes traitées",
        "Requête SQL": "SELECT centre_id, AVG(delai_effectif) AS delai_moyen_jours FROM logs_activite WHERE type_operation='Traitement' GROUP BY centre_id;"
    },
    {
        "Nom du KPI": "KPI 2 : Capacité journalière moyenne",
        "Objectif métier": "Mesurer la performance opérationnelle",
        "Description / Interprétation": "Indique combien de demandes un centre peut traiter en moyenne par jour",
        "Règle de calcul": "Moyenne de nombre_traite par jour",
        "Requête SQL": "SELECT centre_id, AVG(nombre_traite) AS capacite_moyenne_jour FROM logs_activite GROUP BY centre_id;"
    },
    {
        "Nom du KPI": "KPI 3 : Taux de couverture territoriale",
        "Objectif métier": "Évaluer l’accessibilité",
        "Description / Interprétation": "Pourcentage de communes desservies par au moins un centre",
        "Règle de calcul": "(nombre de communes desservies / nombre total de communes) * 100",
        "Requête SQL": "SELECT (COUNT(DISTINCT commune) * 100.0 / (SELECT COUNT(*) FROM details_communes)) AS taux_couverture FROM demandes_service_public JOIN centres_service USING(centre_id);"
    },
    {
        "Nom du KPI": "KPI 4 : Distance moyenne entre centres et communes desservies",
        "Objectif métier": "Évaluer l’accessibilité",
        "Description / Interprétation": "Mesure la proximité moyenne des citoyens aux centres de service",
        "Règle de calcul": "Moyenne des distances km calculées entre centre et commune",
        "Requête SQL": "SELECT AVG(distance_km) AS distance_moyenne_km FROM centres_service JOIN details_communes USING(prefecture);"
    },
    {
        "Nom du KPI": "KPI 5 : Taux de rejet des demandes",
        "Objectif métier": "Qualité de service",
        "Description / Interprétation": "Pourcentage de demandes rejetées par rapport au nombre total de demandes",
        "Règle de calcul": "(SUM(nombre_rejete) / SUM(nombre_traite + nombre_rejete)) * 100",
        "Requête SQL": "SELECT centre_id, (SUM(nombre_rejete)*100.0 / SUM(nombre_traite + nombre_rejete)) AS taux_rejet FROM logs_activite GROUP BY centre_id;"
    },
    {
        "Nom du KPI": "KPI 6 : Charge par personnel",
        "Objectif métier": "Efficience / charge",
        "Description / Interprétation": "Nombre moyen de demandes traitées par agent présent",
        "Règle de calcul": "nombre_traite / personnel_present",
        "Requête SQL": "SELECT centre_id, AVG(nombre_traite / personnel_present) AS charge_moyenne_agent FROM logs_activite GROUP BY centre_id;"
    }
]

# 2️⃣ Transformer en DataFrame pandas
df = pd.DataFrame(kpis)

# 3️⃣ Exporter en Excel
df.to_excel("kpis.xlsx", index=False, engine='openpyxl')

print("✅ Fichier 'kpis.xlsx' créé avec succès !")
