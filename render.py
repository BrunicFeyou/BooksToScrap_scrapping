import csv 
from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


with open('data-live.csv', 'w', encoding='utf-8') as fichier :
    writter = csv.writer(fichier)
    writter.writerow(['product_page_url', 'universal_product_code ', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    one_books_url = soup.select_one('article.product_pod > h3 > a')
    # print(one_books_url)
    new_url = url + '/' + str(one_books_url['href'])
    # print(new_url)
    details_response = requests.get(new_url)
    details_soup = BeautifulSoup(details_response.text, 'html.parser') 
    upc = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type').text
    # print(upc)
    title = details_soup.find('h1').text
    # print (title)
    price_tax = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(4) td:first-of-type').text
    # print(price_tax) 
    price = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(3) td:first-of-type').text
    # print(price)
    number_available = details_soup.select_one('p.instock.availability').text
    # print(number_available)
    product_description = details_soup.select_one('div.container-fluid.page > div.page_inner > div.content > div#content_inner > article.product_page > p').text
    # print(product_description)
    category = details_soup.select_one('ul.breadcrumb > li:nth-child(3) > a').text
    # print(category)
    review_rating = details_soup.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:nth-child(7) td:first-of-type').text
    # print(review_rating)
    image = details_soup.find('img')
    image_link = image['src']
    image_url = url + image_link.replace("../..", "")
    # print(image_url) 
    writter.writerow([new_url,upc,title, price_tax, price, number_available, product_description, category,review_rating, image_url ])
    

    

    