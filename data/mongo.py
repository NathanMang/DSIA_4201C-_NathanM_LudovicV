from pymongo import MongoClient


def get_series_from_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['allocine']
    collection = db['series']
    
    # Récupérer toutes les séries de la collection
    series_data = list(collection.find())

    
        
    client.close()
    return series_data

