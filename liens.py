import json
import time
from tqdm import tqdm  # Pour la barre de progression

# Chemin vers le fichier JSON contenant les données des exercices
input_file = "exercice_fr.json"  # Remplacez par le chemin de votre fichier JSON
output_file = "exercises_updated.json"  # Fichier de sortie avec les liens mis à jour

# URL de base pour les GIFs hébergés sur GitHub Pages
base_url = "https://adam9b.github.io/UrlGit/exercise_gifs/"

# Charger les données JSON
with open(input_file, "r", encoding="utf-8") as f:
    exercises = json.load(f)

# Démarrer le timer
start_time = time.time()

# Parcourir les exercices et mettre à jour les liens des GIFs
for exercise in tqdm(exercises, desc="Mise à jour des liens", unit="exercice"):
    if "gifUrl" in exercise:
        # Extraire l'ID de l'exercice (supposons que l'ID est dans le champ "id")
        exercise_id = exercise["id"]
        # Construire le nouveau lien
        new_gif_url = f"{base_url}{exercise_id}.gif"
        # Mettre à jour le champ "gifUrl"
        exercise["gifUrl"] = new_gif_url

# Sauvegarder les données mises à jour dans un nouveau fichier JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(exercises, f, indent=4, ensure_ascii=False)

# Calculer le temps écoulé
end_time = time.time()
elapsed_time = end_time - start_time

print(f"\nLes liens ont été mis à jour et sauvegardés dans {output_file}.")
print(f"Temps total écoulé : {elapsed_time:.2f} secondes.")