# main.py

import mongoDB

from dashboard.page_router import create_router_page

def main():
    """Fonction principale pour lancer l'application"""
    # Créer l'application à partir du routers
    
    mongoDB.insert_series_db()
    app = create_router_page()
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
