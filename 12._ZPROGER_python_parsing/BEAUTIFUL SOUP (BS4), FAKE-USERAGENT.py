
import requests
from fake_useragent import UserAgent
import fake_useragent
from requests import Session
from bs4 import BeautifulSoup

link = 'https://icanhazip.com/'
link1 = 'https://fin-calc.org.ua/ru/what/is/my/browser/'

user = fake_useragent.UserAgent().random


headers = {
    'User-Agent': user,
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'content-type': 'application/json',
    'Alt-Used': 'toolbox.googleapps.com',
    'Connection': 'keep-alive',
    'Referer': link1,
    # 'Cookie': 'WS_LANG=ru; wt_sessionid=qqivefgqdf2rlpz1ynfcr2stkg1m7syh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


# response = requests.get(link)  # content при скачивании картинкии побайтное скачивание
# print(response.text)

s = Session()
s.headers.update(headers)
response = s.get(link1)

response1 = response.text 
soup = BeautifulSoup(response1, 'lxml')
block = soup.find("span", class_="error")
print(block)

def write_html(value):
    with open("1.html", 'w', encoding="utf-8") as file:
        file.write(response1)

# write_html(response1)