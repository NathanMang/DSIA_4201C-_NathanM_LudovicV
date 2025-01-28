# Utiliser une image Python officielle
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . .

# Définir la commande à exécuter au démarrage du conteneur
CMD ["python", "main.py"]
