import csv 
from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_categories = []
books_url = []
get_all_categories = soup.select('div.side_categories > ul.nav.nav-list > li > ul > li > a')
for get_all_category in get_all_categories : 
    category_name = get_all_category.text.strip()
    all_categories.append((category_name, get_all_category['href']))
    

for category, href in all_categories : 
    if category == 'Womens Fiction' : 
        get_womens_fiction_url = url + '/' + href.strip()
        print(get_womens_fiction_url) 
        category_response = requests.get(get_womens_fiction_url)
        category_soup = BeautifulSoup(category_response.content, 'html.parser')
        women_fiction_books = category_soup.select('li.col-xs-6.col-sm-4.col-md-3.col-lg-3 > article.product_pod > h3 > a')
        for women_fiction_book in women_fiction_books : 
            # print(women_fiction_book['href'])
            women_fiction_book_href = women_fiction_book['href']
            women_fiction_book_link = women_fiction_book_href.replace('../../..', '/catalogue')
            # print(women_fiction_book_link)
            women_fiction_book_url = url + women_fiction_book_link
            books_url.append(women_fiction_book_url)
            print(women_fiction_book_url)

with open('data-live.csv', 'w', encoding='utf-8') as fichier :
    writter = csv.writer(fichier)
    writter.writerow(['product_page_url', 'universal_product_code ', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    for book_url in books_url : 
        # print(one_books_url)
        # print(new_url)
        details_response = requests.get(book_url)
        details_soup = BeautifulSoup(details_response.content, 'html.parser') 
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
        writter.writerow([book_url,upc,title, price_tax, price, number_available, product_description, category,review_rating, image_url ])
    

    


    