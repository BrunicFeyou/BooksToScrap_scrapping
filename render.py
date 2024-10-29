import csv 
from bs4 import BeautifulSoup
import requests
import os 
import shutil
from download_functions import download_images


all_categories = [] # correspond au tableau contenant toutes les catégories avec leurs nom et url

books_url = []  
if books_url : 
    books_url.clear()
#                             Récupérer une catéogorie parmi toutes, des livres et les mettre dans lun fichier csv
def get_data_to_scrap(link) :
        url = link
        try : 
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            get_all_categories = soup.select('div.side_categories > ul.nav.nav-list > li > ul > li > a')
            for get_all_category in get_all_categories : 
                category_name = get_all_category.text.strip()
                if all_categories : 
                    all_categories.clear()
                all_categories.append((category_name, get_all_category['href'])) 
                for category, href in all_categories : 
                    if category == 'Womens Fiction' : 
                        get_womens_fiction_url = url + '/' + href.strip()
                        while get_womens_fiction_url : 
                            try : 
                                category_response = requests.get(get_womens_fiction_url)       
                                category_soup = BeautifulSoup(category_response.content, 'html.parser')
                                women_fiction_books = category_soup.select('li.col-xs-6.col-sm-4.col-md-3.col-lg-3 > article.product_pod > h3 > a')
                                for women_fiction_book in women_fiction_books : 
                                    women_fiction_book_href = women_fiction_book['href']
                                    women_fiction_book_link = women_fiction_book_href.replace('../../..', '/catalogue')
                                    women_fiction_book_url = url + women_fiction_book_link
                                    books_url.append(women_fiction_book_url) 
                                next_page = category_soup.select_one('li.next > a')
                                if next_page:
                                    next_page_url = next_page['href']
                                    get_womens_fiction_url = url + '/' + href.strip() + '/' + next_page_url + '/'
                                    
                                else:
                                    get_womens_fiction_url = None
                                display_data_csv(url)         
                            except Exception as e : 
                                print(f"Vous ne pouvez pas accèder au all_categories maitenant pour cause {e}, revenez plus tard")
                                break                     
                    
        except EOFError as e : 
            print(f"Vous ne pouvez pas accéder à l'url du site initiale maintenant pour cause {e}") 

def display_data_csv (link) :
    with open('data_live.csv', 'w', encoding='utf-8') as fichier :
        writter = csv.writer(fichier)
        writter.writerow(['product_page_url', 'universal_product_code ', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
        for book_url in books_url : 
                try : 
                    details_response = requests.get(book_url)
                    details_soup = BeautifulSoup(details_response.content, 'html.parser') 
                    upc_tag = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type')
                    upc = upc_tag.text if upc_tag else 'Pas de UPC pour ce produit'
                    
                    title = details_soup.find('h1').text
                    
                    price_tax_tag = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(4) td:first-of-type')
                    price_tax = price_tax_tag.text if price_tax_tag else 'Pas de taxes sur le prix de ce produit'
                    
                    price = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(3) td:first-of-type').text
                    
                    number_available = details_soup.select_one('p.instock.availability').text.strip()
                    
                    product_description = details_soup.select_one('div.container-fluid.page > div.page_inner > div.content > div#content_inner > article.product_page > p').text
                   
                    category = details_soup.select_one('ul.breadcrumb > li:nth-child(3) > a').text
                    
                    review_rating = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(7) td:first-of-type').text
                    print(review_rating)
                    image = details_soup.find('img')
                    image_link = image['src']
                    image_url = link + image_link.replace("../..", "")
                    
                    writter.writerow([book_url,upc,title, price_tax, price, number_available, product_description, category,review_rating, image_url ])
                except IndexError as e : 
                    print(f"Vous ne pouvez pas accèdez au lien de tous les books_url parce que {e}")

get_data_to_scrap('https://books.toscrape.com')

#     a partir du fichier csv télécherger les images des photos et les mettre dans un dossier

download_images('./download_all_images/one_category')  

    
 
        


    


    