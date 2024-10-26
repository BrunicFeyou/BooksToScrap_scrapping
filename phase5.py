import csv 
from bs4 import BeautifulSoup
import requests
import os 
import shutil
from download_functions import download_all_categories_images
from urllib.parse import urljoin

array_calcul = []
total_count = 0
counts = 0
column_counts = {}

with open('books_categories.csv', 'r' , encoding='utf-8') as file : 
    library_books = csv.DictReader(file)
    for column in library_books.fieldnames:
        column_counts[column] = 0
    
    # Parcourt chaque ligne et chaque colonne pour vérifier la présence de 'page_url'
    for book in library_books:
        for column, value in book.items():
            if value == 'page_url':  # Vérifie si la valeur correspond exactement à 'page_url'
                column_counts[column] += 1

# Affiche les résultats
for column, count in column_counts.items():
    print(f"'{column}' contient '{count}' occurrences de 'page_url'")


