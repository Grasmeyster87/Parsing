
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.dialog.ua/'

articles = {}

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")
td_list = soup.select('div[class=new-item]')
articles = {td.a.get('href'): td.a.text for td in td_list}


def save_json(name_file):
    # сохранить в json
    with open(name_file, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(articles, ensure_ascii=False))


def dowload_json(name_file):
    # загрузить из json
    with open(name_file, 'r', encoding='utf-8') as fh1:  # открываем файл на чтение
        news1 = json.load(fh1)  # загружаем из файла данные в словарь data

    for key, value in news1.items():
        print("{0}: {1} \n".format(key, value))


# for key, value in articles.items():
#   print("{0}: {1} \n".format(key,value))

save_json('news.json')
dowload_json('news.json')
