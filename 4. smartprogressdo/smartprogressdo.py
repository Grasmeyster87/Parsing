import requests
from bs4 import BeautifulSoup as BS
import fake_useragent
import json

url = 'https://smartprogress.do/?lang=ru'

user = fake_useragent.UserAgent().random

headers = {
    
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'PHPSESSID=8eebv4hsnhp0ppll9sf84ki0i8; language-guest=d8e8a5ea72107805aedf701baf03f251b21a7d9bs%3A2%3A%22ru%22%3B; YII_CSRF_TOKEN=948347e36bb3f733737992e576a24d7d1bc09b23s%3A40%3A%222fb701b67081df5817b86481268b202460338f18%22%3B; _ga=GA1.2.1085840768.1744656233; _gid=GA1.2.1075786082.1744656233; _gat=1; _ga_T9HTM0LFD0=GS1.2.1744656232.1.0.1744656232.0.0.0',

}

s = requests.Session()
s.headers.update(headers)

# get CSRF

auth_html = s.get(url)
auth_bs = BS(auth_html.content, 'html.parser')


# csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']
input_tag = auth_bs.find('input', {'name': 'YII_CSRF_TOKEN'})
name_value = input_tag.get('value')

print(name_value)

# do login
payload = {
    "YII_CSRF_TOKEN": name_value,
    "returnUrl": '/',
    "UserLoginForm[email]": "azal11@meta.ua",
    "UserLoginForm[password]": "[Azal_job11]",
    "UserLoginForm[rememberMe]": 1
}

answ = s.post('https://smartprogress.do/?lang=ru', data=payload)
answ_bs = BS(answ.content, "html.parser")
# print(answ_bs.find_all("div", class_="contentuser-menu__name"))
# print(answ_bs)

def save_html(page, content):
    with open(f"page.html", mode='w', encoding="utf-8") as file:
        file.write(str(answ_bs))
        print(f"Данные сохранены в файл {page}.html")

save_html('1', answ_bs)