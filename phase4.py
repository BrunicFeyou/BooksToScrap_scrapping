import csv 
from bs4 import BeautifulSoup
import requests
import os 


folder_images = './download_all_images'
if not os.path.exists(folder_images):
    os.makedirs(folder_images)

url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_categories = []
books_url = []

#                 Récupérer toutes les catéogories ds livres et les mettre dans le fichier csv data-live
# get_all_categories = soup.select('div.side_categories > ul.nav.nav-list > li > ul > li > a')
# for get_all_category in get_all_categories : 
#     category_name = get_all_category.text.strip()
#     all_categories.append((category_name, get_all_category['href']))    

# for category, href in all_categories :   
#     get_all_url = url + '/' + href.strip()
#     # print(get_all_url) 
#     category_response = requests.get(get_all_url)
#     category_soup = BeautifulSoup(category_response.content, 'html.parser')
#     all_categories_books = category_soup.select('li.col-xs-6.col-sm-4.col-md-3.col-lg-3 > article.product_pod > h3 > a')
#     for all_category_book in all_categories_books : 
#         # print(women_fiction_book['href'])
#         category_book_href = all_category_book['href']
#         category_book_name = all_category_book.text
#         category_book_link = category_book_href.replace('../../..', '/catalogue')
#         # print(women_fiction_book_link)
#         category_book_url = url + category_book_link
#         books_url.append((category_book_name, category_book_url))
#         # print(category_book_name, category_book_url) 

# with open('books_categories.csv', 'w', encoding='utf-8') as fichier :
#     writter = csv.writer(fichier)
#     writter.writerow(['product_page_url', 'universal_product_code ', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
#     for book_name, book_url in books_url : 
#         # print(one_books_url)
#         # print(new_url)
#         details_response = requests.get(book_url)
#         details_soup = BeautifulSoup(details_response.content, 'html.parser') 
#         upc = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type').text
#         # print(upc)
#         title = details_soup.find('h1').text
#         print (title)
#         price_tax = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(4) td:first-of-type').text
#         # print(price_tax) 
#         price = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(3) td:first-of-type').text
#         # print(price)
#         number_available = details_soup.select_one('p.instock.availability').text.strip()
#         # print(number_available)
#         product_description_tag = details_soup.select_one('div.container-fluid.page > div.page_inner > div.content > div#content_inner > article.product_page > p')
#         product_description = product_description_tag.text if product_description_tag else 'Description non disponible'
#         # print(product_description)
#         category = details_soup.select_one('ul.breadcrumb > li:nth-child(3) > a').text 
#         # print(category)
#         review_rating = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(7) td:first-of-type').text
#         # print(review_rating)
#         image = details_soup.find('img')
#         image_link = image['src']
#         image_url = url + image_link.replace("../..", "") 
#         # print(image_url) 
#         writter.writerow([book_url,upc,title, price_tax, price, number_available, product_description, category,review_rating, image_url ])

# with open('books_categories.csv', 'r', encoding='utf-8') as file: 
#     contains_folder = csv.DictReader(file) 
#     for contain in contains_folder: 
#         image_url = contain['image_url']
#         print(image_url)
#         try:   
#             response = requests.get(image_url)
#             extension = image_url.split('.')[-1]
#             filename = os.path.join(folder_images, f"image_{contains_folder.line_num}.{extension}")
#             with open(filename, "wb") as fichier:
#                 fichier.write(response.content)
#                 # print(f"Image téléchargée et renommée: {filename}")         
#         except Exception as e:
#             print(f"Erreur lors du téléchargement de {image_url}: {e}") 