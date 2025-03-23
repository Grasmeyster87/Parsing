import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as BS
import json

url1 = 'https://stopgame.ru/articles'

articles = {}

headers = {'User-Agent': 'Mozilla/5.0'}
# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.text, "html.parser")
# td_list = soup.select('a[class=_title_1lcny_24]')
# articles = {a.get('href'): a.text for a in td_list}

# for key, value in articles.items():
#   print("https://stopgame.ru{0}: {1} \n".format(key,value))

# -------------------------------------------------------------
page = 0
count = 0


def save_json(name_file):
    # сохранить в json
    with open(name_file, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(articles, ensure_ascii=False))


while True:
    if page < 272:
        if page == 0:
            url = url1
            page += 1
        else:
            url = url1+f"/p{page}"
            page += 1

        r = requests.get(url, headers=headers)
        html = BS(r.content, 'html.parser')
        items = html.select("a[class=_title_1lcny_24]")

        if (len(items)):
            for el in items:
                count += 1
                articles[f"page № {page} - {count}"] = f"https://stopgame.ru{el.get('href')} - {el.text}"
                print({key: value for key, value in articles.items()})
                save_json('stopgameru.json')
                # print('page №', page, count, 'https://stopgame.ru',
                #       el.get('href'), ' : ', el.text, '\n')
        else:
            break

    else:
        break
