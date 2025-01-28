import dash
from dash import html

def create_home_layout():
    """Retourne la mise en page améliorée de la page d'accueil"""
    return html.Div(children=[
        # Section de titre avec fond coloré et ombre portée
        html.Div([
            html.H1("Bienvenue sur l'application Dash", 
                    style={
                        "text-align": "center", 
                        "color": "#ffffff",  # Couleur du texte
                        "font-family": "Arial, sans-serif",  # Police moderne
                        "font-size": "3em",  # Taille de la police
                        "margin-top": "20px",
                        "text-shadow": "2px 2px 5px rgba(0, 0, 0, 0.3)"  # Ombre du texte
                    }),
            html.P("Affichage dynamique des séries avec Dash!", 
                   style={
                       "text-align": "center",
                       "color": "#eeeeee",  # Texte plus clair
                       "font-size": "1.5em",  # Taille de la police
                       "margin-bottom": "40px",
                   })
        ], style={
            "background-color": "#3b3b3b",  # Fond sombre
            "padding": "40px 20px",  # Espacement intérieur
            "border-radius": "10px",  # Bords arrondis
        }),

        # Ajouter un footer en bas de la page
        html.Footer(children=[
            html.P("© 2025 - Séries Allociné - Mang Nathan & Ludovic Viellard", style={
                "text-align": "center",
                "font-size": "14px",
                "color": "gray",
                "margin-top": "20px"
            }),
            
        ], style={
            "position": "fixed",
            "bottom": "0",
            "width": "100%",
            "background-color": "#f8f8f8",
            "padding": "10px 0",
            "box-shadow": "0 -2px 5px rgba(0, 0, 0, 0.1)"
        }),

        # Ajout d'une section pour des boutons interactifs ou des liens
        html.Div([
            html.Button("Explorer les Séries", 
                        id="explore-button",
                        style={
                            "display": "block",
                            "width": "250px",  # Largeur du bouton
                            "margin": "20px auto",  # Centrer le bouton
                            "padding": "15px",
                            "background-color": "#ff7f50",  # Couleur du bouton
                            "color": "white",  # Texte blanc
                            "font-size": "1.2em",  # Taille de la police
                            "border": "none",
                            "border-radius": "5px",  # Bords arrondis
                            "cursor": "pointer",  # Curseur pointer pour l'interaction
                        })
        ], style={
            "text-align": "center",  # Centrer les éléments
        }),

    ], style={
        "font-family": "Arial, sans-serif",  # Police générale
        "padding": "20px",  # Espacement global
        "background-color": "#f7f7f7",  # Fond clair pour la page
    })
