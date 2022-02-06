import csv
from bs4 import BeautifulSoup
from config import Config
import requests


def create_file():
    file = open(Config.FILE_URL, 'w')
    csvwriter = csv.writer(file)
    csvwriter.writerow(['title', 'price', 'description'])
    file.close()


def get_count_of_pages(content):
    soup = BeautifulSoup(content, 'html.parser')
    pagination_list = soup.find(class_='pagination')
    last_el = pagination_list.find_all('li')[-1].find('a')
    link = last_el['href']
    return link[-1]


def save_row(data):
    file = open(Config.FILE_URL, 'a')
    writer = csv.writer(file)
    writer.writerows(data)
    writer.writerow('\n')
    file.close()


def get_content(url, page_number):
    link_page = url
    if page_number != "":
        link_page = url + "?page=" + str(page_number)
    response = requests.get(link_page)
    return response.content


def get_description(href):
    content = get_content(href, '')
    soup = BeautifulSoup(content, 'html.parser')
    all_items = soup.find_all(class_='description__text js-hidden-content')
    items_list = []
    for item in all_items:
        items_list.append(item.text)
    return items_list


def get_all_items():
    response = requests.get(Config.PARSING_URL)
    count_of_pages = get_count_of_pages(response.content)
    for page_number in range(1, int(count_of_pages) + 1):
        items_list = []
        content = get_content(Config.PARSING_URL, page_number)
        soup = BeautifulSoup(content, 'html.parser')
        all_items = soup.find_all(class_='catalog-item__entry')
        for item in all_items:
            title_object = item.find(class_='catalog-item__title')
            title = title_object.find('a').text
            href = title_object.find('a').get('href')
            description = get_description(href)
            price = item.find(class_='catalog-item__price').text

            print(title)
            print(price)
            print(description)
            items_list.append([title, price, description])
        save_row(items_list)
