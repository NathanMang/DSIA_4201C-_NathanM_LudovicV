from dash import Input, Output
from mongoDB import get_series_from_db
from dashboard import dataFormat

def register_callbacks(app):
    """Enregistre tous les callbacks de l'application."""

    @app.callback(
        Output('series-table', 'data'),
        [Input('sort-by-dropdown', 'value')]
    )
    def sort_series(sort_by):
        series_data = get_series_from_db()

        # Trier les séries en fonction du critère sélectionné
        if sort_by == 'title':
            sorted_data = sorted(series_data, key=lambda x: x['title'])
        elif sort_by == 'ranking':
            sorted_data = sorted(series_data, key=lambda x: x['ranking'], reverse=True)  # Tri par classement décroissant
        elif sort_by == 'country':
            sorted_data = sorted(series_data, key=lambda x: x['country'])
        else:
            sorted_data = series_data  # Si aucune colonne n'est sélectionnée, ne rien trier

        return dataFormat(sorted_data)
