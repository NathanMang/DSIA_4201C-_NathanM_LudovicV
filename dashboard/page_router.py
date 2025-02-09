"""Page router"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dashboard.series_page import create_series_page  
from dashboard.home_page import create_home_page
from dashboard.map_page import create_map_page

def create_router_page():
    """Création du routeur pour les pages"""

    # Créer l'application
    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    
    # Créer le contenu de la page
    app.layout = html.Div(style={"font-family": "Arial, sans-serif", "background-color": "#f7f7f7", "min-height": "100vh"}, children=[
        dcc.Location(id='url', refresh=False),

        html.Nav(style={
            # Style de la barre de navigation
            "background-color": "#3b3b3b",  # Fond 
            "padding": "10px 20px",  # Espacement 
            "border-radius": "5px",  # Bords arrondis
            "margin-bottom": "20px"  # Marge pour séparer la navigation du contenu
        }, children=[ # Liste des liens
            dcc.Link('Accueil', href='/', id='link-home', style={
                "color": "white",  
                "margin-right": "20px",  
                "font-size": "1.2em",  
                "text-decoration": "none",  
                "transition": "color 0.3s",
            }),
            dcc.Link('Séries', href='/series', id='link-series', style={
                "color": "white",
                "margin-right": "20px",
                "font-size": "1.2em",
                "text-decoration": "none",
                "transition": "color 0.3s",
            }),
            dcc.Link('Carte', href='/carte', id='link-map', style={
                "color": "white",
                "font-size": "1.2em",
                "text-decoration": "none",
                "transition": "color 0.3s",
            }),
        ]),

        html.Div(id='page-content', style={
            "padding": "0 20px",  
            "text-align": "center",  
        })
    ])
    
    # Callback pour afficher la page selon l'URL et gérer l'état des liens actifs
    @app.callback(
        [Output('page-content', 'children'),
         Output('link-home', 'style'),
         Output('link-series', 'style'),
         Output('link-map', 'style')],
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        # Définir les styles des liens en fonction de la page active
        link_style = {
            "color": "white",  
            "margin-right": "20px",  
            "font-size": "1.2em",  
            "text-decoration": "none",  
            "transition": "color 0.3s",
        }

        active_style = {
            "color": "#ffdd00",  # Jaune pour indiquer l'état actif
            "margin-right": "20px",  
            "font-size": "1.2em",  
            "text-decoration": "none",  
            "transition": "color 0.3s",
        }

        # Gérer l'affichage de la page en fonction de l'URL
        if pathname == '/':
            return create_home_page(), active_style, link_style, link_style  # Page d'accueil active
        elif pathname == '/series':
            return create_series_page(), link_style, active_style, link_style  # Page des séries active
        elif pathname == '/carte':
            return create_map_page(app), link_style, link_style, active_style  # Page de la carte active
        else:
            return html.H1("404 - Page non trouvée", style={"color": "red"}), link_style, link_style, link_style

    return app
