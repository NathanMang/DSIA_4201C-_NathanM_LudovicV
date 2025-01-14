# dashboard/home_page.py

import dash
from dash import html

def create_home_layout():
    """Retourne la mise en page de la page d'accueil"""
    return html.Div(children=[
        html.H1("Bienvenue sur l'application Dash", style={"text-align": "center"}),
        html.P("Affichage dynamique des séries avec Dash!", style={"text-align": "center"}),
    ])
