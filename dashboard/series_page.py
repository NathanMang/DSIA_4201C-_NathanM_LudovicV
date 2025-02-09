"""Series page"""

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
from mongoDB import get_series_from_db
from dashboard.dataFormat import format_data  


def create_series_page():
    """Page pour afficher les séries avec une fonctionnalité de recherche et de tri"""

    # Récupérer les séries depuis MongoDB
    series_data = get_series_from_db()

    # Colonnes du tableau
    columns = [
        {'name': 'Classement', 'id': 'ranking'},
        {'name': 'Titre', 'id': 'title'},
        {'name': 'Genres', 'id': 'genres'},
        {'name': 'Réalisateur', 'id': 'creator'},
        {'name': 'Acteurs', 'id': 'actors'},
        {'name': 'Note de presse', 'id': 'press_rating'},
        {'name': 'Note des spectateurs', 'id': 'audience_rating'},
        {'name': 'Pays', 'id': 'country'},
    ]
    
    initial_data = format_data(series_data)

    # Layout de la page
    layout = html.Div([
        html.H1("Séries du site Allocine", style={'textAlign': 'center'}),

        # Barre de recherche
        html.Div([
            dcc.Input(
                id='search-input',
                type='text',
                placeholder='Rechercher une série, acteur, créateur...',
                style={'margin-right': '10px', 'width': '300px'}
            ),
            # Dropdown pour le tri
            dcc.Dropdown(
                id='sort-by-dropdown',
                options=[
                    {'label': 'Titre', 'value': 'title'},
                    {'label': 'Note', 'value': 'audience_rating'},
                    {'label': 'Pays', 'value': 'country'},
                ],
                style={'width': '200px', 'margin-top': '10px', 'margin-left': '10px'}
            ),
        ], style={'margin-bottom': '20px', 'textAlign': 'center'}),

        # Tableau interactif
        dash_table.DataTable(
            id='series-table',
            columns=columns,
            data=initial_data,
            page_size=15,
            style_table={'height': '350px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'},
            markdown_options={"link_target": "_blank"},
        ),
    ])

    return layout

def create_series_callback(app):

    # Callback pour filtrer les résultats et trier
    @app.callback(
        Output('series-table', 'data'),
        [Input('search-input', 'value'), Input('sort-by-dropdown', 'value')],   
    )
    def update_table(search_value, sort_by):
        series_data = get_series_from_db()

        # Filtrer les séries en fonction du mot-clé de recherche
        if search_value:
            series_data = [
                series for series in series_data
                if search_value.lower() in series.get('title', '').lower()
                or any(search_value.lower() in genre.lower() for genre in series.get('genres', []))
                or any(search_value.lower() in creator.lower() for creator in series.get('creator', []))
                or any(search_value.lower() in actor.lower() for actor in series.get('actors', []))
            ]

        # Trier les séries en fonction du critère sélectionné
        if sort_by == 'title':
            series_data = sorted(series_data, key=lambda x: x['title'])
        elif sort_by == 'ranking':
            series_data = sorted(series_data, key=lambda x: x['ranking'], reverse=True)
        elif sort_by == 'country':
            series_data = sorted(series_data, key=lambda x: x['country'])

        return format_data(series_data)
