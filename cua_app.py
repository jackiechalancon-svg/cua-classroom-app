import streamlit as st

st.title("Diagnostic CUA de la classe")

st.write("Créatrice de l'application : Jacky Chalancon")

st.write("Cette application permettra d'analyser le profil cognitif général d'une classe et l'environnement capacitant.")
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Diagnostic CUA", layout="wide")

st.title("Diagnostic CUA de la classe")
st.write("Créatrice de l'application : Jacky Chalancon")

st.header("1. Profil cognitif général de la classe")

st.write("Évaluez les besoins cognitifs globaux de votre classe.")

def question(label, explanation):
    st.markdown("**" + label + "**")
    st.caption(explanation)
    return st.slider(label,1,5,3)

attention = question(
"Attention",
"Exemple : élèves facilement distraits ou difficulté à maintenir l'attention."
)

memoire = question(
"Mémoire de travail",
"Exemple : élèves qui oublient les étapes d'une consigne."
)

comprehension = question(
"Compréhension",
"Exemple : élèves ayant besoin d'exemples ou de reformulations."
)

motivation = question(
"Motivation / Engagement",
"Exemple : participation faible ou abandon rapide."
)

planification = question(
"Planification (fonctions exécutives)",
"Exemple : difficulté à organiser le travail."
)

sensorialite = question(
"Sensorialité",
"Certains élèves apprennent mieux avec des images (visuel), d'autres en écoutant (auditif) ou en manipulant (kinesthésique)."
)

autoregulation = question(
"Autorégulation émotionnelle",
"Gestion de la frustration et des émotions face aux difficultés."
)

st.header("2. Environnement capacitant de la classe")

st.write("Évaluez dans quelle mesure l'environnement pédagogique favorise l'accès aux apprentissages.")

supports = st.slider("Variété des supports pédagogiques",1,5,3)
autonomie = st.slider("Autonomie des élèves",1,5,3)
evaluation = st.slider("Flexibilité de l'évaluation",1,5,3)
modalites = st.slider("Diversité des modalités d'apprentissage",1,5,3)

if st.button("Lancer le diagnostic CUA"):

    profil = {
        "Attention":attention,
        "Mémoire":memoire,
        "Compréhension":comprehension,
        "Motivation":motivation,
        "Planification":planification,
        "Sensorialité":sensorialite,
        "Autorégulation":autoregulation
    }

    st.header("Profil cognitif de la classe")

    df = pd.DataFrame(profil.items(), columns=["Dimension","Score"])
    st.table(df)

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(profil.values())+[list(profil.values())[0]],
        theta=list(profil.keys())+[list(profil.keys())[0]],
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(range=[0,5])),
        showlegend=False,
        title="Radar cognitif de la classe"
    )

    st.plotly_chart(fig)

    engagement = motivation
    representation = (comprehension + memoire)/2
    action_expression = (planification + sensorialite)/2

    radar_cua = {
        "Engagement":engagement,
        "Représentation":representation,
        "Action / Expression":action_expression
    }

    st.header("Radar CUA")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatterpolar(
        r=list(radar_cua.values())+[list(radar_cua.values())[0]],
        theta=list(radar_cua.keys())+[list(radar_cua.keys())[0]],
        fill='toself'
    ))

    fig2.update_layout(
        polar=dict(radialaxis=dict(range=[0,5])),
        showlegend=False
    )

    st.plotly_chart(fig2)

    score_env = round(np.mean([supports, autonomie, evaluation, modalites])*20)

    st.header("Score environnement capacitant")

    st.write(score_env,"/100")

    score_cua = round((engagement+representation+action_expression)/3*20)

    st.header("Score global CUA")

    st.write(score_cua,"/100")

    st.header("Aménagements pédagogiques possibles")

    recommandations=[]

    if comprehension>3:
        recommandations.append("Utiliser des supports multimodaux : schémas, vidéos, exemples.")

    if attention>3:
        recommandations.append("Segmenter les consignes et proposer des étapes visuelles.")

    if planification>3:
        recommandations.append("Utiliser des checklists et modèles de tâches.")

    if motivation>3:
        recommandations.append("Introduire des choix d'activités pour renforcer l'engagement.")

    if sensorialite>3:
        recommandations.append("Varier manipulation, discussion et schémas.")

    if autoregulation>3:
        recommandations.append("Prévoir des pauses ou outils de gestion des émotions.")

    for r in recommandations:
        st.write("-",r)

    st.header("Simulateur de séance CUA")

    objectif = st.text_input("Objectif pédagogique")
    notion = st.text_input("Notion étudiée")

    if st.button("Générer une séance adaptée"):

        st.subheader("Structure de séance proposée")

        st.write("Engagement")
        st.write("- question problème")
        st.write("- activité collaborative")

        st.write("Représentation")
        st.write("- schéma explicatif")
        st.write("- vidéo courte")

        st.write("Action / Expression")
        st.write("- production écrite")
        st.write("- présentation orale")
