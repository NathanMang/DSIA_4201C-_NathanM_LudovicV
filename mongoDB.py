from pymongo import MongoClient
from scrappingAllocine import get_series_info

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['allocine']
series_collection = db['series']

def insert_series_db():
    base_url = "https://www.allocine.fr/series/meilleures/"
    
    series_collection.delete_many({})
    # Récupérer les séries pour la page 1
    series_data_list = get_series_info(base_url)
    
    # Insérer les données récupérées dans MongoDB si elles n'existent pas déjà
    for series_data in series_data_list:
        title = series_data.get('title', '')
        
        # Vérifier si une série avec ce titre existe déjà dans la base de données
        existing_series = series_collection.find_one({'title': title})
        
        # Si la série n'existe pas on ajoute
        if not existing_series:
            series_collection.insert_one(series_data)

    
    for page_number in range(2, 4):  
        url = f"{base_url}?page={page_number}"
        series_data_list = get_series_info(url)
        
        for series_data in series_data_list:
            title = series_data.get('title', '')
            
            # Vérifier si une série avec ce titre existe déjà dans la base de données
            existing_series = series_collection.find_one({'title': title})
            
            # Si la série n'existe pas on ajoute
            if not existing_series:
                series_collection.insert_one(series_data)

def get_series_from_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['allocine']
    collection = db['series']
    
    # Récupérer toutes les séries de la collection
    series_data = list(collection.find())
    client.close()
    return series_data

if __name__ == '__main__':
    insert_series_db()
