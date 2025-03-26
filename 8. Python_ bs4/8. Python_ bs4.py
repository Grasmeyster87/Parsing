import requests
from bs4 import BeautifulSoup
from time import sleep

url_quotes_toscrape = 'https://quotes.toscrape.com/'

list_card_url = []

count_card = 1

for count in range(1, 8):

    sleep(3)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://scrapingclub.com/exercise/list_basic/?page={count}',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    url_scrapingclub = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url_scrapingclub, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')  # html.parser

    data_card = soup.find_all("div", class_="w-full rounded border")

    for i in data_card:
        card_url = 'https://scrapingclub.com' + i.find('a').get("href")
        print(card_url)
        list_card_url.append(card_url)

    """
        # получение данных с промо карты товара
        # name = i.find("h4").text.replace('\n', '')  # text получение текста replace('\n', '') убираем пренос строк
        # price = i.find('h5').text
        # url_img = 'https://scrapingclub.com' + i.find('img', class_="card-img-top img-fluid").get('src')

        # count_card += 1
        # print(count_card, name + "\n" + price + "\n" + url_img + "\n\n")
    
    """
