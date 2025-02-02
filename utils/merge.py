from PIL import Image
import os
import re

# Paramètres
MERGED_OUTPUT_FOLDER = "merged_spritesheets"  # Dossier contenant les spritesheets
GLOBAL_SPRITESHEET_OUTPUT = "global_spritesheet.png"  # Nom du fichier de sortie
SPRITE_WIDTH = 64  # Largeur d'un spritesheet (3 sprites de 16px)
SPRITE_HEIGHT = 24  # Hauteur d'un sprite

def extract_numbers(filename):
    """Extrait les numéros de colonne et de fin du fichier."""
    match = re.search(r'column_(\d+)_.*_(\d+)\.png$', filename)
    if match:
        column_number = int(match.group(1))  # Numéro de colonne
        end_number = int(match.group(2))  # Numéro de fin
        return end_number, column_number
    return float('inf'), float('inf')

def create_global_spritesheet(input_folder, output_file, sprite_width, sprite_height):
    # Récupérer tous les spritesheets
    spritesheets = sorted(
        [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".png")],
        key=lambda x: extract_numbers(os.path.basename(x))  # Tri par numéro de fin PUIS par colonne
    )

    if not spritesheets:
        print(f"⚠️ Aucun spritesheet trouvé dans {input_folder}.")
        return

    # Calculer les dimensions du spritesheet global
    total_width = sprite_width  # Largeur fixe (3 sprites de large)
    total_height = sprite_height * len(spritesheets)  # Une ligne par spritesheet

    # Créer une image vide pour le spritesheet global
    global_spritesheet = Image.new("RGBA", (total_width, total_height))

    # Remplir le spritesheet global
    for index, sheet_path in enumerate(spritesheets):
        sheet = Image.open(sheet_path)
        global_spritesheet.paste(sheet, (0, index * sprite_height))

    # Sauvegarder l'image finale
    global_spritesheet.save(output_file)
    print(f"✅ Spritesheet global généré : {output_file}")

# Exécution du script
create_global_spritesheet(MERGED_OUTPUT_FOLDER, GLOBAL_SPRITESHEET_OUTPUT, SPRITE_WIDTH, SPRITE_HEIGHT)
