import csv 
from bs4 import BeautifulSoup
import requests
import os 
import shutil
from download_functions import download_all_categories_images
from urllib.parse import urljoin
import re 
import time

all_categories = []
books_url = []

#                 Récupérer toutes les catéogories et toutes les informations de tous les livres et les mettre dans le fichier csv data-live
def get_all_categories_data(link):
    url = link
    all_categories = []  
    books_url = []  
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        get_all_categories = soup.select('div.side_categories > ul.nav.nav-list > li > ul > li > a')
        for get_all_category in get_all_categories:
            category_name = get_all_category.text.strip()
            category_href = get_all_category['href']
            all_categories.append((category_name, category_href))  
        for category, href in all_categories:
            get_all_url = urljoin(url, href.strip())
            while get_all_url:
                try:
                    loop_pages(get_all_url, url, books_url)  
                    category_response = requests.get(get_all_url)
                    category_soup = BeautifulSoup(category_response.content, 'html.parser')
                    next_page = category_soup.select_one('li.next > a')
                    if next_page:
                        next_page_url = next_page['href']
                        get_all_url = urljoin(get_all_url, next_page_url)
                        
                    else:
                        
                        break

                except Exception as e:
                    print(f"Could not access categories due to: {e}. Try again later.")
                    break
            # After fetching all pages in a category, call get_all_books_data
    except requests.exceptions.RequestException as e:
        print(f"Could not access the initial URL due to: {e}")
    get_all_books_data(books_url)


def loop_pages(get_all_url, url, books_url):
    try:
        category_response = requests.get(get_all_url)
        category_soup = BeautifulSoup(category_response.content, 'html.parser')
        all_categories_books = category_soup.select('li.col-xs-6.col-sm-4.col-md-3.col-lg-3 > article.product_pod > h3 > a')
        for all_category_book in all_categories_books:
            category_book_href = all_category_book['href']
            category_book_name = all_category_book.text
            category_book_link = category_book_href.replace('../../..', '/catalogue')
            category_book_url = urljoin(url, category_book_link)
            books_url.append((category_book_name, category_book_url))
    except requests.exceptions.RequestException as e:
        print(f"Error in fetching page data due to: {e}")
        

def get_all_books_data(books_url):  # books_url ajouté comme paramètre
    with open('books_categories.csv', 'w', encoding='utf-8') as fichier:
        writter = csv.writer(fichier)
        writter.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

        for book_name, book_url in books_url:
            try:
                    details_response = requests.get(book_url)
                    details_soup = BeautifulSoup(details_response.content, 'html.parser')
                    upc = details_soup.select_one('table > tr:nth-child(1) > td').text  # Sélecteur CSS simplifié pour upc
                    title = details_soup.find('h1').text
                    print(upc)
                    price_tax = details_soup.select_one('table > tr:nth-child(4) > td').text  # Sélecteur CSS simplifié pour price_tax
                    price = details_soup.select_one('table > tr:nth-child(3) > td').text  # Sélecteur CSS simplifié pour price
                    number_available = details_soup.select_one('p.instock.availability').text.strip()
                    # pattern = r"\w+ (\d{2} \w)"
                    # number_available_regex = re.search(pattern,number_available_tag)
                    # if number_available_regex : 
                    #     number_available = number_available_regex.group(1)
                    #     print(number_available)
                    product_description_tag = details_soup.select_one('article.product_page > p')
                    product_description = product_description_tag.text if product_description_tag else 'Description not available'
                    category = details_soup.select_one('ul.breadcrumb > li:nth-child(3) > a').text
                    review_rating = details_soup.select_one('table > tr:nth-child(7) > td').text  # Sélecteur CSS simplifié pour review_rating
                    image = details_soup.find('img')
                    image_url = urljoin(book_url, image['src'])  # Utilisation de urljoin pour image_url
                    writter.writerow([book_url, upc, title, price_tax, price, number_available, product_description, category, review_rating, image_url])
            except Exception as e:
                    print(f"Error accessing book details due to: {e}")
                   



get_all_categories_data('https://books.toscrape.com')
download_all_categories_images('./download_all_images/all_categories')

# http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
# http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html
# http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html
# http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html