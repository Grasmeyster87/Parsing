from requests import Session
from bs4 import BeautifulSoup
import time, random

base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://scrapingclub.com/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.2100364150.1742975485; _ga_BD9ZHFE1XX=GS1.1.1743154933.4.1.1743155099.0.0.0',
}


def main_write_html(base_url):
    s = Session()
    s.headers.update(headers)
    response = s.get(base_url)
    with open('data.html', 'w', encoding='utf-8') as r:
        r.write(response.text)

def main_card_name_price(base_url):
    s = Session()
    s.headers.update(headers)
    response = s.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all("div",  class_="w-full rounded border post")

    for card in cards:
        name = card.find('h4').find('a').text
        price = card.find('h5').text
        print(name)
        print(price)

def main(base_url):
    s = Session()
    s.headers.update(headers)
    count = 1
    pagination = 0
    while True:

        
        url = base_url + '?page=' + str(count)
       
        print(url)


        response = s.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        if count == 1:
            pagination = int(soup.find("nav", class_="pagination").find_all("span", class_="page")[-2].text)
            print(pagination)
        
        cards = soup.find_all("div",  class_="w-full rounded border post")

        for card in cards:
            name = card.find('h4').find('a').text
            price = card.find('h5').text
            print(name)
            print(price)

        print(count)
        count += 1
        time.sleep(random.choice([5, 7, 9]))
        if count == pagination:
            break

    


main(base_url)

