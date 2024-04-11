from pdf2image import convert_from_path
import os


basePath = os.path.dirname(os.path.realpath(__file__))
print(basePath)

# Convertir le PDF en une liste d'images
base_filename = "file"
file_name = os.path.join(basePath, f"../files/{base_filename}.pdf")
images = convert_from_path(file_name)

# Enregistrer les images dans des fichiers
for i, image in enumerate(images):
    dest_filename = os.path.join(basePath, f"../files/{base_filename}{i}.png")
    image.save(dest_filename, 'PNG')
