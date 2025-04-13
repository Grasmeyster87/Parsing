import requests
from bs4 import BeautifulSoup as BS
import fake_useragent
import json

url = 'https://smartprogress.do/?lang=ru'

user = fake_useragent.UserAgent().random

headers = {
    'User-Agent': user,
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'content-type': 'application/json',
    'Alt-Used': 'toolbox.googleapps.com',
    'Connection': 'keep-alive',
    'Referer': url,
    # 'Cookie': 'WS_LANG=ru; wt_sessionid=qqivefgqdf2rlpz1ynfcr2stkg1m7syh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

s = requests.Session()
s.headers.update(headers)

# get CSRF

auth_html = s.get(url)
auth_bs = BS(auth_html.content, 'html.parser')


csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']
# print(csrf)

# do login
payload = {
    "YII_CSRF_TOKEN": csrf,
    "returnUrl": '/',
    "UserLoginForm[email]": "azal11@meta.ua",
    "UserLoginForm[password]": "[Azal_job11]",
    "UserLoginForm[rememberMe]": 1
}

answ = s.post('https://smartprogress.do/?lang=ru', data=payload)
answ_bs = BS(answ.content, "html.parser")
# print(answ_bs.find_all("div", class_="contentuser-menu__name"))
print(answ_bs)

def save_html(page, content):
    with open(f"page.html", mode='w', encoding="utf-8") as file:
        file.write(str(answ_bs))
        print(f"Данные сохранены в файл {page}.html")

save_html('1', answ_bs)