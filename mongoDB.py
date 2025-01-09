from pymongo import MongoClient
from scrappingAllocine import get_series_info

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['allocine']
series_collection = db['series']

def insert_series_db():
    base_url = "https://www.allocine.fr/series/meilleures/"
    print("Page 1")
    series_data_list = get_series_info(base_url)
    
    # Insérer les données récupérées dans MongoDB
    for series_data in series_data_list:
        series_collection.insert_one(series_data)
        print(f"Insertion dans MongoDB : {series_data['title']}")

    # Pages suivantes
    for page_number in range(2, 4):  
        url = f"{base_url}?page={page_number}"
        print(f"\nPage {page_number}...")
        series_data_list = get_series_info(url)
        
        for series_data in series_data_list:
            series_collection.insert_one(series_data)
            print(f"Insertion dans MongoDB : {series_data['title']}")

if __name__ == '__main__':
    insert_series_db()
