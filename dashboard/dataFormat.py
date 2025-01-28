
# Affichage du tableau sur la page
def format_data(series_data):
    data = []
    for series in series_data:
        url = series.get('url', '')
        if url and not url.startswith('https://'):
            url = f'https://www.allocine.fr{url}'
        data.append({
            'title': series.get('title', 'Non spécifié'),
            'ranking': series.get('ranking', 'Non spécifié'),
            'genres': series.get('genres', []),
            'creator': ', '.join(series.get('creator', [])),
            'actors': ', '.join(series.get('actors', [])),
            'press_rating': series.get('press_rating', 'Non spécifié'),
            'audience_rating': series.get('audience_rating', 'Non spécifié'),
            'url': f'{url}',
            'country': series.get('country', 'Pays non trouvé'),
        })
    return data