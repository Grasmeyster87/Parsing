import requests
from bs4 import BeautifulSoup
import csv
from model import Product


articles = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '
    'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def parser(url: str, max_item: int):
    create_csv()

    page = 1
    count_items = 0

    while max_item > count_items:

        list_product = []
        # res = requests.get(url=url, proxies=proxies, headers=headers)
        # res = requests.get(f"{url}&p={page}", params=payloads_, timeout=150, headers=headers)
        res = requests.get(f"{url}&p={page}", headers=headers, timeout=150)

        print(res.url)

        soup = BeautifulSoup(res.text, "lxml")
        products = soup.find_all("div", class_="product-card oneclick-enabled")

        for product in products:

            if count_items >= max_item:
                break

            count_items += 1
            name = product.get("data-product-brand")
            sku = product.find("span", class_="product-card__key").text

            name_elem = product.find("div", class_="product-card__name")
            link = name_elem.find("a").get("href")

            price_teg = product.find("div", class_="product-card__price")
            price = price_teg.findAll("span", class_="num")[0].get("content")

            if (price != True):
                price = "По запросу"
            list_product.append(Product(sku=sku,
                                        name=name,
                                        link=link,
                                        price=price))

        write_csv(list_product)
        page += 1


def create_csv():
    with open(f"glavsnab.csv", mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sku", "name", "link", "price"])


def write_csv(products: list[Product]):
    with open(f"glavsnab.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.sku, product.name,
                            product.link, product.price])


if __name__ == "__main__":
    # parser(url="https://glavsnab.net/santehnika/rakoviny-i-komplektuyushchiye/rakoviny.html?limit=100", max_item=180)
    parser(url="https://glavsnab.net/santehnika/rakoviny-i-komplektuyushchiye/rakoviny.html", max_item=60) # сайт не подгружает всю информацию
    
