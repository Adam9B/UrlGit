import requests
import shutil
import os
import time
from tqdm import tqdm  # Pour la barre de progression

# Configuration de l'API
url = "https://exercisedb.p.rapidapi.com/exercises"
querystring = {"limit": "1400", "offset": "0"}
headers = {
    "x-rapidapi-key": "ce982b25b5mshe18b0e703d6e083p1668f9jsn858855faeb91",  # Remplacez par votre clé API
    "x-rapidapi-host": "exercisedb.p.rapidapi.com"
}

# Démarrer le timer
start_time = time.time()

# Envoyer la requête à l'API
response = requests.get(url, headers=headers, params=querystring)

# Vérifier si la requête a réussi
if response.status_code == 200:
    exercises = response.json()  # Récupérer les données JSON

    # Créer un dossier pour stocker les GIFs
    if not os.path.exists("exercise_gifs"):
        os.makedirs("exercise_gifs")

    # Initialiser le compteur de GIFs téléchargés
    downloaded_gifs = 0

    # Barre de progression avec tqdm
    for exercise in tqdm(exercises, desc="Téléchargement des GIFs", unit="gif"):
        gif_url = exercise.get("gifUrl")  # Récupérer l'URL du GIF
        if gif_url:
            exercise_id = exercise["id"]  # Récupérer l'ID de l'exercice
            try:
                # Télécharger le GIF
                gif_response = requests.get(gif_url, stream=True)
                if gif_response.status_code == 200:
                    # Sauvegarder le GIF dans un fichier
                    with open(f"exercise_gifs/{exercise_id}.gif", "wb") as f:
                        shutil.copyfileobj(gif_response.raw, f)
                    downloaded_gifs += 1
                else:
                    print(f"Erreur lors du téléchargement du GIF pour l'exercice {exercise_id}")
            except Exception as e:
                print(f"Erreur pour l'exercice {exercise_id} : {e}")
else:
    print(f"Erreur lors de la requête API : {response.status_code}")

# Arrêter le timer et afficher le temps écoulé
end_time = time.time()
elapsed_time = end_time - start_time

# Résumé des résultats
print(f"\nTéléchargement terminé !")
print(f"Nombre de GIFs téléchargés : {downloaded_gifs}")
print(f"Temps écoulé : {elapsed_time:.2f} secondes")