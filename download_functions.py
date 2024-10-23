import os
import shutil
import csv 
import requests


#  a partir du fichier csv télécherger les images des photos et les mettre dans un dossier

def download_images(folder) : 
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
    with open('data_live.csv', 'r', encoding='utf-8') as file: 
        contains_folder = csv.DictReader(file) 
        for contain in contains_folder: 
            image_url = contain['image_url']
            # print(image_url)
            try:   
                response = requests.get(image_url)
                extension = image_url.split('.')[-1]
                filename = os.path.join(folder, f"Womens_Fiction_Couverture{contains_folder.line_num}.{extension}")
                if os.path.exists(filename) :
                    os.remove(file)
                elif not os.path.exists(filename) :   
                    with open(filename, "wb") as fichier:
                        fichier.write(response.content)
            except Exception as e : 
                print(f"Erreur lors du téléchargement de {image_url}: {e}")