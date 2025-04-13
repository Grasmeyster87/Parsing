import requests

import csv
import time

from model import Product
from savers import save_html, create_csv
from page_hadler import page_hadler

articles = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '
    'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url="https://radiodetali.com.ua/ua/catalog/kondensatory"

def parser(url: str, max_item: int):
    create_csv()
    page = 1
    count_items = 1
    counter = 1
    list_product = []
    while max_item > count_items:

        res = requests.get(f"{url}?p={page}", headers=headers, timeout=150)

        # print(res)
        # print(res.url)
        list_product, counter = page_hadler(page, res, max_item, list_product, count_items, counter)
        
        print(list_product)
        page += 1
        time.sleep(3)
        write_csv(list_product)
        list_product.clear()
        count_items += 1
        # print(list_product)


def write_csv(list_product):
    with open(f"./glavsnab.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for product in list_product:
            writer.writerow(product.values())

            
if __name__ == "__main__":
    # parser(url="https://glavsnab.net/santehnika/rakoviny-i-komplektuyushchiye/rakoviny.html?limit=100", max_item=180)
    parser(url=url, max_item=9) # сайт не подгружает всю информацию
    
