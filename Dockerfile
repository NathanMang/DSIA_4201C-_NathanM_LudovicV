# Utilisation d'une image Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source dans le conteneur
COPY . .

# Exposer le port sur lequel Dash fonctionne
EXPOSE 8050

# Commande pour démarrer l'application
CMD ["python", "main.py"]
