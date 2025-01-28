import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from mongoDB import get_series_from_db

def create_map_page(app):
    """Page pour afficher la carte des pays"""

    # Récupérer les séries depuis MongoDB
    series_data = get_series_from_db()

    # Extraire les pays
    countries = [series.get('country') for series in series_data]
    country_counts = {country: countries.count(country) for country in set(countries)}

    # Convertir en DataFrame pour Plotly
    country_df = pd.DataFrame(list(country_counts.items()), columns=['Country', 'Count'])

    # Créer la carte choroplèth
    fig = px.choropleth(country_df, 
                        locations="Country", 
                        locationmode="country names",
                        color="Count",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        color_continuous_midpoint=0.5,
                        title="Répartition des séries par pays",
                        )  

    # Ajouter des réglages pour améliorer l'apparence
    fig.update_geos(showcoastlines=True, coastlinecolor="lightgray", showland=True, landcolor="whitesmoke")
    fig.update_layout(
        title_font=dict(size=24, color="black"),  # Couleur du titre en noir pour plus de contraste
        coloraxis_colorbar_title="Nombre de Séries",
        margin={"r":0, "t":30, "l":0, "b":0},  # Réduit les marges pour un aspect plus compact
        paper_bgcolor="white",  # Fond blanc autour de la carte
        plot_bgcolor="white",   # Fond blanc dans la zone de la carte
    )

    # Layout de la page
    return html.Div([
        html.H1("Carte des séries par pays", style={
            'textAlign': 'center',
            'color': 'black',  # Texte noir pour contraster avec le fond clair
            'font-family': 'Arial, sans-serif',
            'font-size': '28px',
            'margin-bottom': '20px'
        }),

        # Affichage de la carte
        dcc.Graph(
            id='country-map',
            figure=fig
        ),
    ])
