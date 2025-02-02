from PIL import Image
import os

# Paramètres à modifier selon ton besoin
SPRITESHEET_PATH = "../small_rpg/textures/original_characters.png"  # Chemin du spritesheet
SPRITE_WIDTH = 16  # Largeur d'un sprite
SPRITE_HEIGHT = 24  # Hauteur d'un sprite
OUTPUT_FOLDER = "output_sprites"  # Dossier de sortie

def extract_sprites(spritesheet_path, sprite_width, sprite_height, output_folder):
    # Ouvrir le spritesheet
    spritesheet = Image.open(spritesheet_path)
    sheet_width, sheet_height = spritesheet.size

    # Créer le dossier de sortie principal s'il n'existe pas
    os.makedirs(output_folder, exist_ok=True)

    columns = sheet_width // sprite_width  # Nombre de colonnes
    rows = sheet_height // sprite_height  # Nombre de lignes

    for col in range(columns):
        # Créer un sous-dossier pour chaque colonne
        col_folder = os.path.join(output_folder, f"column_{col}")
        os.makedirs(col_folder, exist_ok=True)

        for row in range(rows):
            x = col * sprite_width
            y = row * sprite_height

            # Extraire le sprite
            sprite = spritesheet.crop((x, y, x + sprite_width, y + sprite_height))
            sprite.save(os.path.join(col_folder, f"sprite_{row}.png"))

    print(f"Extraction terminée : {columns} colonnes créées dans {output_folder}")

# Exécution du script
extract_sprites(SPRITESHEET_PATH, SPRITE_WIDTH, SPRITE_HEIGHT, OUTPUT_FOLDER)
