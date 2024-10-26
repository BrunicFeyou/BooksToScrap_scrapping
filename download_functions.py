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
            file_name = contain['title']
            # print(image_url)
            try:   
                response = requests.get(image_url)
                extension = image_url.split('.')[-1]
                filename = os.path.join(folder, f"{file_name}.{extension}")
                if os.path.exists(filename) :
                    os.remove(file)
                elif not os.path.exists(filename) :   
                    with open(filename, "wb") as fichier:
                        fichier.write(response.content)
            except Exception as e : 
                print(f"Erreur lors du téléchargement de {image_url}: {e}")

def download_all_categories_images(folder_images) :
    if os.path.exists(folder_images):
        shutil.rmtree(folder_images)
    os.makedirs(folder_images)
    with open('books_categories.csv', 'r', encoding='utf-8') as file: 
        contains_folder = csv.DictReader(file) 
        for contain in contains_folder: 
            image_url = contain['image_url']
            file_name = contain['title']
            # print(image_url)
            try:   
                response = requests.get(image_url)
                extension = image_url.split('.')[-1]
                filename = os.path.join(folder_images, f"{file_name}.{extension}")
                if os.path.exists(filename) :
                    os.remove(file)
                elif not os.path.exists(filename) :   
                    with open(filename, "wb") as fichier:
                        fichier.write(response.content)        
            except Exception as e:
                print(f"Erreur lors du téléchargement de {image_url}: {e}") 