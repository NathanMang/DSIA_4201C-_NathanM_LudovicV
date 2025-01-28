import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_series_info(url):
    try:
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

                # Récupérer l'URL de la page de détails (URL relative)
                url_series = serie.find('a', class_='meta-title-link')
                url_series = url_series['href'] if url_series else 'URL non trouvée'
                
                # Convertir l'URL relative en URL absolue
                url_series = urljoin(url, url_series) if url_series != 'URL non trouvée' else 'URL non trouvée'

                rating_items = serie.find_all('div', class_='rating-item')

                press_rating = 'Non disponible'
                audience_rating = 'Non disponible'

                for rating_item in rating_items:
                    if 'Presse' in rating_item.text:
                        press_note = rating_item.find('span', class_='stareval-note')
                        press_rating = press_note.text.strip() if press_note else 'Non disponible'
                    elif 'Spectateurs' in rating_item.text:
                        audience_note = rating_item.find('span', class_='stareval-note')
                        audience_rating = audience_note.text.strip() if audience_note else 'Non disponible'

                # Récupérer la nationalité des séries
                series_details = get_series_details(url_series)

                series_data = {
                    'title': title,
                    'ranking': ranking,
                    'genres': genres,
                    'creator': creator,
                    'actors': actors,
                    'press_rating': press_rating,
                    'audience_rating': audience_rating,
                    'url': url_series,
                    'country': series_details.get('country', 'Pays non trouvé'),
                }
                
                series_data_list.append(series_data)

            return series_data_list  # Retourner la liste des données des séries
    
        else:
            print(f"Erreur: La page {url} n'a pas pu être chargée. Code statut: {response.status_code}")
            return []
    except Exception as e:
        print(f"Une erreur s'est produite lors de la récupération des données pour {url}: {e}")
        return []



def get_series_details(url):
    """Récupère les détails de la série à partir de son URL"""
    response = requests.get(url)
    if response.status_code != 200:
        return {}

    page_soup = BeautifulSoup(response.text, 'html.parser')
    country_tag = page_soup.find('div', class_='meta-body-item meta-body-nationality')
    country = country_tag.find('span', class_='dark-grey-link').text.strip() if country_tag else 'Pays non trouvé'
    
    return {'country': country}


