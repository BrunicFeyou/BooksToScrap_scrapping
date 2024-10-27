import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from matplotlib_graph import graphique1
from matplotlib_graph import graphique2

def draw_limited_string(c, text, y, max_width, x=50, font="Helvetica", font_size=12):
    c.setFont(font, font_size)
    words = text.split(' ')
    line = ''
    
    for word in words:
        # Calculer la largeur de la ligne avec le nouveau mot ajouté
        test_line = f"{line} {word}".strip()
        if c.stringWidth(test_line, font, font_size) <= max_width:
            line = test_line
        else:
            # Dessiner la ligne précédente et recommencer
            c.drawString(x, y, line)
            y -= font_size + 2  # Espacement entre les lignes
            line = word  # Commencer une nouvelle ligne avec le mot courant
            
    # Dessiner la dernière ligne
    if line:
        c.drawString(x, y, line)



pdf_path = "./rapport_graphiques.pdf" 

c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.drawString(150, 750,"Rapport des prix des livres d'occasion")

description_text2 = ("Le diagramme présentant la moyenne des livres par catégorie offre une vue d'ensemble des différents genres littéraires et de leur popularité relative en termes de nombre de titres disponibles. Chaque catégorie, qu'il s'agisse de romans, de science-fiction, de biographies ou d'autres genres, est représentée de manière distincte, ce qui permet d'identifier facilement les segments où l'offre est la plus importante. Ce visuel aide non seulement à comprendre la diversité des livres, mais également à analyser les tendances du marché de l'édition, en mettant en lumière les catégories qui attirent le plus l'attention des lecteurs.")

image2 = ImageReader(graphique2)
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 700, "Le prix moyen des livres par catégorie (Graphique 1)")
c.setFont("Helvetica", 8)
draw_limited_string(c, description_text2, 680, max_width=500)
c.drawImage(image2, 50, 280, width=500, height=300)

c.showPage()

description_text1 = "Le graphique en barre illustrant la moyenne des prix des livres par catégorie fournit une perspective précieuse sur les variations de prix entre les différents genres littéraires. Les barres, colorées de manière à distinguer chaque catégorie, montrent clairement les différences significatives des prix moyens, permettant ainsi aux lecteurs de mieux comprendre le positionnement économique de chaque type de livre. Par exemple, on peut observer que certains genres, comme les manuels scolaires ou les livres spécialisés, affichent des prix plus élevés en moyenne, tandis que d'autres, comme les romans de fiction générale, tendent à être plus abordables. Ce graphique aide les acheteurs potentiels à évaluer leurs options et à faire des choix éclairés en fonction de leur budget et de leurs préférences littéraires."

image1 = ImageReader(graphique1)
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 700, "Le pourcentage de livres par catégories (Graphique )") 
c.setFont("Helvetica", 8)
draw_limited_string(c, description_text1, 680, max_width=500)
c.drawImage(image1, 50, 280, width=500, height=300)



c.showPage()
c.save()





# print(f"PDF généré avec succès : {pdf_path}")