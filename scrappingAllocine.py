import requests
from bs4 import BeautifulSoup


def get_series_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Extraire toutes les cartes de séries
        series= soup.find_all('div', class_='card entity-card entity-card-list cf')
        
        for serie in series:

            # Titre
            title = serie.find('h2', class_='meta-title')
            title = title.text.strip() if title else 'Titre non trouvé'

            # Classement
            ranking = serie.find('div', class_='label-ranking')
            ranking = ranking.text.strip() if ranking else 'Non spécifié'
        
                     
           # Extraire les genres
            genres = []
            genre_section = serie.find('div', class_='meta-body-item meta-body-info')
            if genre_section:
                genre_elements = genre_section.find_all('span', class_='dark-grey-link')
                for genre in genre_elements:
                    genres.append(genre.text.strip())
            
            genres = ', '.join(genres) if genres else 'Genre non spécifié'
            
            # Extraire le créateur
            creators = []
            creator_section = serie.find('div', class_='meta-body-item meta-body-direction')
            if creator_section:
                creator_element = creator_section.find_all('span', class_='dark-grey-link')
                for creator in creator_element:
                    creators.append(creator.text.strip())
            
            creator = creators if creator else 'Créateur non spécifié'
            
            # Extraire les acteurs principaux
            actors = []
            actor_section = serie.find('div', class_='meta-body-item meta-body-actor')
            if actor_section:
                actor_elements = actor_section.find_all('span', class_='dark-grey-link')
                for actor in actor_elements[:3]:  # Prendre les 3 premiers acteurs
                    actors.append(actor.text.strip())
                 
            
            # Extraire les notes
            rating_items = serie.find_all('div', class_='rating-item')
            
            # Initialiser les notes
            press_rating = 'Note de presse non disponible'
            audience_rating = 'Note des spectateurs non disponible'

            for rating_item in rating_items:
                # Chercher la note de presse 
                if 'Presse' in rating_item.text:
                    press_note = rating_item.find('span', class_='stareval-note')
                    press_rating = press_note.text.strip() if press_note else 'Note de presse non disponible'
                
                # Chercher la note des spectateurs 
                elif 'Spectateurs' in rating_item.text:
                    audience_note = rating_item.find('span', class_='stareval-note')
                    audience_rating = audience_note.text.strip() if audience_note else 'Note des spectateurs non disponible'

            # Informations
            print(f"Classement : {ranking}")
            print(f"Titre : {title}")
            print(f"Genre : {genres}")
            print(f"Créateur : {', '.join(creator)}")
            print(f"Acteurs : {', '.join(actors)}")
            print(f"Note de presse : {press_rating}")
            print(f"Note des spectateurs : {audience_rating}")

            
            print("="*50)  
            
    else:
        print(f"Erreur: La page {url} n'a pas pu être chargée. Code statut: {response.status_code}")


def main():
    # URL de base pour la première page
    base_url = "https://www.allocine.fr/series/meilleures/"
    
    # Première page
    print("Récupération des informations de la page 1...")
    get_series_info(base_url)
    
    # Pages suivantes
    for page_number in range(2, 4):  
        url = f"{base_url}?page={page_number}"
        print(f"\nRécupération des informations de la page {page_number}...")
        get_series_info(url)

if __name__ == '__main__':
    main()
