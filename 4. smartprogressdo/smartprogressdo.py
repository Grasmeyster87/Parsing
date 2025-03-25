import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as BS
import json

url = 'https://smartprogress.do/?lang=ru'

s = requests.Session()

# get CSRF

auth_html = s.get(url)
auth_bs = BS(auth_html.content, "html.parser")
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

# парсит неудачно https://smartprogress.do/?lang=ru
# print(answ_bs.select("div", class_=['user-menu__name']))
# print("Имя: {}\nУровень: {}\nОпыт: {}".format(
#     answ_bs.select(".user-menu__name")[0].text.strip(),
#     answ_bs.select(
#         ".user-menu__info-text user-menu__info-text--lvl")[0].text.strip(),
#     answ_bs.select(
#         ".user-menu__info-text user-menu__info-text--exp")[0].text.strip(),
# ))
