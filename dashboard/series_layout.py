from dash import html, dcc
import dash_table
import pandas as pd
from mongoDB import get_series_from_db

def create_layout(app):
    """Définit la mise en page de l'application."""
    
    # Récupérer les séries depuis MongoDB
    series_data = get_series_from_db()

    # Extraire les pays et formater les données pour le tableau
    data = format_data(series_data)

    # Dropdown pour trier les séries
    sort_by_dropdown = dcc.Dropdown(
        id='sort-by-dropdown',
        options=[
            {'label': 'Titre', 'value': 'title'},
            {'label': 'Classement', 'value': 'ranking'},
            {'label': 'Pays', 'value': 'country'}
        ],
        placeholder="Trier par...",
    )

    return html.Div([
        html.H1("Séries TV", style={'textAlign': 'center'}),
        
        # Dropdown pour trier les séries
        html.Div([
            html.Label("Trier les séries par :"),
            sort_by_dropdown
        ], style={'width': '300px', 'margin': '20px auto'}),

        # Tableau des séries
        dash_table.DataTable(
            id='series-table',
            columns=[
                {'name': 'Titre', 'id': 'Titre'},
                {'name': 'Classement', 'id': 'Classement'},
                {'name': 'Pays', 'id': 'Pays'}
            ],
            data=data,
            filter_action='native',  # Permet de filtrer les données dans le tableau
            sort_action='native',    # Permet de trier par colonne directement
            sort_mode='multi',       # Permet un tri multiple
            style_table={'marginTop': '20px'},
        ),
    ])

def format_data(series_data):
    """Formatte les données pour le tableau"""
    return [{
        'Titre': series['title'],
        'Classement': series['ranking'],
        'Pays': series['country'],
    } for series in series_data]
