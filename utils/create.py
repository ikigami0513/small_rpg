import re
from PIL import Image
import os

# Paramètres
OUTPUT_FOLDER = "output_sprites"  # Dossier contenant les sous-dossiers des colonnes
MERGED_OUTPUT_FOLDER = "merged_spritesheets"  # Dossier où seront stockés les nouveaux spritesheets
SPRITE_WIDTH = 16  # Largeur d'un sprite
SPRITE_HEIGHT = 24  # Hauteur d'un sprite

def extract_number(filename):
    """Extrait le premier nombre trouvé dans un nom de fichier."""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')  # Place en dernier si pas de nombre

def create_spritesheets_from_columns(input_folder, output_folder, sprite_width, sprite_height):
    # Créer le dossier de sortie
    os.makedirs(output_folder, exist_ok=True)

    # Parcourir chaque colonne (sous-dossier)
    for col_folder in sorted(os.listdir(input_folder)):
        col_path = os.path.join(input_folder, col_folder)

        if not os.path.isdir(col_path):
            continue  # Ignorer les fichiers qui ne sont pas des dossiers

        # Récupérer tous les fichiers images et les trier numériquement
        sprites = sorted(
            [os.path.join(col_path, f) for f in os.listdir(col_path) if f.endswith(".png")],
            key=lambda x: extract_number(os.path.basename(x))  # Tri basé sur le nombre
        )

        # Vérifier qu'on a suffisamment de sprites
        if len(sprites) < 7:
            print(f"⚠️ Pas assez de sprites dans {col_folder}, ignoré.")
            continue

        # Construire des spritesheets en ignorant le premier sprite et en regroupant 3 par 3
        index = 0
        for i in range(1, len(sprites) - 2, 4):  # Commence à 1, saute 1 sprite après chaque batch de 3
            selected_sprites = sprites[i:i + 3]

            # Vérifier qu'on a bien 3 sprites
            if len(selected_sprites) != 3:
                break

            # Créer un nouveau spritesheet
            spritesheet = Image.new("RGBA", (sprite_width * 4, sprite_height))

            # Ajouter les 3 sprites côte à côte
            for j, sprite_path in enumerate(selected_sprites):
                sprite = Image.open(sprite_path)
                spritesheet.paste(sprite, (j * sprite_width, 0))

            sprite = Image.open(selected_sprites[1])
            spritesheet.paste(sprite, (3 * sprite_width, 0))

            # Sauvegarder le spritesheet
            spritesheet_path = os.path.join(output_folder, f"{col_folder}_sheet_{index}.png")
            spritesheet.save(spritesheet_path)
            index += 1

    print(f"✅ Spritesheets générés dans {output_folder}")

# Exécution du script
create_spritesheets_from_columns(OUTPUT_FOLDER, MERGED_OUTPUT_FOLDER, SPRITE_WIDTH, SPRITE_HEIGHT)
