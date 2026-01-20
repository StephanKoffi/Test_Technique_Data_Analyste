# dashboard_global.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Chemins des fichiers nettoyés
clean_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'nettoyees')


# --- Configuration de la page ---
st.set_page_config(page_title="Dashboard Global", layout="wide")

# --- Sidebar pour navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisir le dataset :", 
                        ["Logs Activité", 
                         "Données Socio-économiques", 
                         "Réseau Routier", 
                         "Documents Administratifs"])

# ========================
# PAGE 1 : Logs Activité
# ========================
if page == "Logs Activité":
    logs = pd.read_csv(os.path.join(clean_data_dir, "cleaned_logs_activite.csv"))
    logs['date_operation'] = pd.to_datetime(logs['date_operation'])
    
    st.title("Dashboard Logs d'Activité")

    # KPI
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Délai moyen (jours)", f"{logs['delai_effectif'].mean():.2f}")
    col2.metric("Total demandes traitées", logs['nombre_traite'].sum())
    col3.metric("Total rejets", logs['nombre_rejete'].sum())
    col4.metric("Temps d'attente moyen (min)", f"{logs['temps_attente_moyen_minutes'].mean():.2f}")

    # Filtres
    centre_filtre = st.multiselect("Centres", logs['centre_id'].unique(), default=logs['centre_id'].unique())
    type_doc_filtre = st.multiselect("Type de document", logs['type_document'].dropna().unique(), default=logs['type_document'].dropna().unique())
    logs_filtrés = logs[(logs['centre_id'].isin(centre_filtre)) & (logs['type_document'].isin(type_doc_filtre))]

    # Visualisations
    fig1 = px.bar(logs_filtrés, x='type_document', y='nombre_traite', color='centre_id', barmode='group',
                  title="Volume de demandes par document et centre")
    st.plotly_chart(fig1)

    fig2 = px.line(logs_filtrés.groupby('date_operation')['nombre_traite'].sum().reset_index(),
                   x='date_operation', y='nombre_traite', title="Évolution des demandes traitées")
    st.plotly_chart(fig2)

# ================================
# PAGE 2 : Données Socio-économiques
# ================================
elif page == "Données Socio-économiques":
    df_socio = pd.read_csv(os.path.join(clean_data_dir, "cleaned_donnees_socioeconomiques.csv"))
    
    st.title("Dashboard Données Socio-économiques")
    
    # KPI
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Population totale", df_socio['population'].sum())
    col2.metric("Revenu moyen (FCFA)", f"{df_socio['revenu_moyen_fcfa'].mean():.0f}")
    col3.metric("Taux alphabétisation moyen (%)", f"{df_socio['taux_alphabétisation'].mean():.2f}")
    col4.metric("Densité moyenne (hab/km²)", f"{df_socio['densite'].mean():.0f}")

    # Visualisations
    fig1 = px.bar(df_socio, x='region', y='population', color='region', text_auto=True, title="Population par région")
    st.plotly_chart(fig1)

    fig2 = px.bar(df_socio, x='commune', y='revenu_moyen_fcfa', color='region', title="Revenu moyen par commune")
    st.plotly_chart(fig2)

# ========================
# PAGE 3 : Réseau Routier
# ========================
elif page == "Réseau Routier":
    df_routes = pd.read_csv(os.path.join(clean_data_dir, "cleaned_reseau_routier.csv"))

    st.title("Dashboard Réseau Routier")

    # KPI
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Longueur totale (km)", df_routes['longueur_km'].sum())
    col2.metric("Temps moyen de parcours (h)", f"{df_routes['temps_parcours_heures'].mean():.2f}")
    col3.metric("Points de contrôle totaux", df_routes['points_controle'].sum())
    col4.metric("Passagers par jour (total)", df_routes['passagers_par_jour'].sum())

    # Visualisations
    fig1 = px.pie(df_routes, names='type_route', values='longueur_km', title="Longueur totale par type de route")
    st.plotly_chart(fig1)

    fig2 = px.bar(df_routes, x='nom_route', y='temps_parcours_heures', color='etat_route', title="Temps de parcours par route")
    st.plotly_chart(fig2)

# ================================
# PAGE 4 : Documents Administratifs
# ================================
elif page == "Documents Administratifs":
    df_docs = pd.read_csv(os.path.join(clean_data_dir, "cleaned_documents_administratifs.csv"))
    
    st.title("Dashboard Documents Administratifs")

    # KPI
    col1, col2, col3 = st.columns(3)
    col1.metric("Total documents", df_docs.shape[0])
    col2.metric("Documents par jour (moyenne)", df_docs['nombre_demandes'].mean())
    col3.metric("Taux de rejet moyen (%)", df_docs['taux_rejet_moyen'].mean())

    # Visualisations
    fig1 = px.bar(df_docs, x='type_document', y='nombre_demandes', color='type_document', title="Volume par type de document")
    st.plotly_chart(fig1)
