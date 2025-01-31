import json
from deep_translator import GoogleTranslator
from tqdm import tqdm  # Pour la barre de progression (optionnel)
import time

def translate_text(text, translator, max_retries=3):
    """Traduit un texte avec gestion des erreurs et réessais"""
    for _ in range(max_retries):
        try:
            return translator.translate(text)
        except Exception as e:
            print(f"Erreur de traduction: {e}. Nouvel essai...")
            time.sleep(1)
    return text  # Retourne l'original si échec après plusieurs tentatives

def translate_bodypart_and_equipment(input_file):
    # Charger les données
    with open(input_file, 'r', encoding='utf-8') as f:
        exercises = json.load(f)

    # Initialiser le traducteur
    translator = GoogleTranslator(source='auto', target='fr')

    # Traduire uniquement bodyPart et equipment
    for exercise in tqdm(exercises, desc="Traduction de bodyPart et equipment"):
        try:
            # Traduire bodyPart
            exercise['bodyPart'] = translate_text(exercise['bodyPart'], translator)
            
            # Traduire equipment
            exercise['equipment'] = translate_text(exercise['equipment'], translator)
            
        except Exception as e:
            print(f"Erreur avec l'exercice {exercise.get('id', 'inconnu')}: {e}")

    # Sauvegarder les résultats dans le même fichier
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(exercises, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    translate_bodypart_and_equipment('exercice_fr.json')