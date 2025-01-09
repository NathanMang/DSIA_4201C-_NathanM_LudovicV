import requests
from bs4 import BeautifulSoup

def get_series_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        series = soup.find_all('div', class_='card entity-card entity-card-list cf')
        
        series_data_list = []  # Liste pour stocker les données des séries

        for serie in series:
            title = serie.find('h2', class_='meta-title')
            title = title.text.strip() if title else 'Titre non trouvé'

            ranking = serie.find('div', class_='label-ranking')
            ranking = ranking.text.strip() if ranking else 'Non spécifié'

            genres = []
            genre_section = serie.find('div', class_='meta-body-item meta-body-info')
            if genre_section:
                genre_elements = genre_section.find_all('span', class_='dark-grey-link')
                for genre in genre_elements:
                    genres.append(genre.text.strip())
            genres = ', '.join(genres) if genres else 'Genre non spécifié'

            creators = []
            creator_section = serie.find('div', class_='meta-body-item meta-body-direction')
            if creator_section:
                creator_element = creator_section.find_all('span', class_='dark-grey-link')
                for creator in creator_element:
                    creators.append(creator.text.strip())
            creator = creators if creators else 'Créateur non spécifié'

            actors = []
            actor_section = serie.find('div', class_='meta-body-item meta-body-actor')
            if actor_section:
                actor_elements = actor_section.find_all('span', class_='dark-grey-link')
                for actor in actor_elements[:3]:  # Prendre les 3 premiers acteurs
                    actors.append(actor.text.strip())

            rating_items = serie.find_all('div', class_='rating-item')

            press_rating = 'Note de presse non disponible'
            audience_rating = 'Note des spectateurs non disponible'

            for rating_item in rating_items:
                if 'Presse' in rating_item.text:
                    press_note = rating_item.find('span', class_='stareval-note')
                    press_rating = press_note.text.strip() if press_note else 'Note de presse non disponible'
                elif 'Spectateurs' in rating_item.text:
                    audience_note = rating_item.find('span', class_='stareval-note')
                    audience_rating = audience_note.text.strip() if audience_note else 'Note des spectateurs non disponible'

            series_data = {
                'title': title,
                'ranking': ranking,
                'genres': genres,
                'creator': creator,
                'actors': actors,
                'press_rating': press_rating,
                'audience_rating': audience_rating
            }

            series_data_list.append(series_data)

        return series_data_list  # Retourner la liste des données des séries
    
    else:
        print(f"Erreur: La page {url} n'a pas pu être chargée. Code statut: {response.status_code}")
        return []

