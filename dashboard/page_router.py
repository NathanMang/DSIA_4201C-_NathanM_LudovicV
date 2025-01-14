# dashboard/page_router.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dashboard.series_page import create_series_page  
from dashboard.home_page import create_home_layout

def create_router_page():
    """Création du routeur pour les pages"""

    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    
    app.layout = html.Div(children=[
        dcc.Location(id='url', refresh=False),
        html.Nav(children=[
            dcc.Link('Accueil', href='/'),
            dcc.Link('Séries', href='/series'),
            # Ajouter les autres liens ici
        ]),
        
        html.Div(id='page-content')
    ])
    
    @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return create_home_layout()  # Page d'accueil
        elif pathname == '/series':
            return create_series_page()  # Page des séries
        else:
            return html.H1("404 - Page non trouvée")

    return app
