import dash
from dash import html,dash_table
from dash.dependencies import Input, Output

from data.mongo import get_series_from_db  #fonction importé

def create_series_page():
    """Page pour afficher les séries"""
    
    series_data = get_series_from_db()  # Récupérer les séries depuis MongoDB
    
    # Colonnes du tableau
    columns = [
        {'name': 'Titre', 'id': 'title'},
        {'name': 'Classement', 'id': 'ranking'},
        {'name': 'Genres', 'id': 'genres'},
        {'name': 'Créateur', 'id': 'creator'},
        {'name': 'Acteurs', 'id': 'actors'},
        {'name': 'Note de presse', 'id': 'press_rating'},
        {'name': 'Note des spectateurs', 'id': 'audience_rating'}
    ]
    
    # Données du tableau
    data = []
    for series in series_data:
        data.append({
            'title': series.get('title', 'Non spécifié'),
            'ranking': series.get('ranking', 'Non spécifié'),
            'genres': series.get('genres', []),
            'creator': series.get('creator', []),
            'actors': ', '.join(series.get('actors', [])),
            'press_rating': series.get('press_rating', 'Non spécifié'),
            'audience_rating': series.get('audience_rating', 'Non spécifié')
        })
    
    # Layout de la page
    layout = html.Div([
        html.H1("Séries du site Allocine", style={'textAlign': 'center'}),
        dash_table.DataTable(
            id='series-table',
            columns=columns,
            data=data,
            style_table={'height': '350px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
        ),
    ])
    
    return layout
