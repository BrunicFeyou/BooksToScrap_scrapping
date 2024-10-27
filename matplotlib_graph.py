import csv 
from bs4 import BeautifulSoup
import requests
import os 
import shutil
from download_functions import download_all_categories_images
from urllib.parse import urljoin
import matplotlib.pyplot as plt 
import numpy as np

category_counts = {}
all_books_count = 0
sum_price = {}
category_counts_percent = {}
middle_price = {}

with open('books_categories.csv', 'r' , encoding='utf-8') as file : 
    library_books = csv.DictReader(file)

    # /////////////////////////////////////////// Graphique circulaire //////////////////////////////////
    for books in library_books : 
        category = books['category']
        price = books["price_excluding_tax"]
        all_books_count +=1 
        if category in category_counts :
            category_counts[category] +=1     
        else : 
            category_counts[category] = 1 
        # /////////////////////////////////////////// Graphique en barre //////////////////////////////////
        price_value = float(price.replace('£', ''))
        if category in sum_price :   
            sum_price[category] += price_value
        else : 
            sum_price[category] = price_value     


    # ////////////////////////////////// calcul su pourcentage de livre et de la moyenne des prix /////////////////////////
    for category, count in category_counts.items() :
        category_counts_percent[category] = (count*100)/all_books_count
        for category_price, price in sum_price.items() : 
            if category_price == category : 
                middle_price[category_price] = round(price/count, 2)
  
    # ////////////////////////////////// Affichage du diagramme circulaire ///////////////////////////////
    explode = [.2 if category == 'Womens Fiction' else .1 for category in category_counts_percent.keys()]
    plt.title("Le pourcentage de livres par catégorie")
    plt.pie(
        category_counts_percent.values(), 
        labels = category_counts_percent.keys(),
        autopct="%.2f%%", 
        explode=explode,
        # shadow=True,
        startangle=90     
    )
    plt.axis("equal")
    graphique1 = "./graphiques_images/graphique_circulaire.png" 
    plt.savefig(graphique1)
    plt.close()

    # ////////////////////////////////////////// Affichache du diagramme en barre ////////////////////////

    plt.title('Le prix moyen des livres par catégorie')
    width = .5
    plt.bar(
        x = middle_price.keys(),
        height = middle_price.values(), 
        width= width, 
        color = 'pink'  
    ) 
    positions = np.arange(len(middle_price))
    plt.xticks(positions, list(middle_price.keys()), rotation=90)
    plt.xlim( - 0.5, len(middle_price) -0.5) 
    plt.xlabel('Catégories')
    plt.ylabel('Prix moyens')
    plt.axis("equal")
    plt.tight_layout()
    graphique2 = "./graphiques_images/graphique_barre.png" 
    plt.savefig(graphique2)
    plt.close()




  





