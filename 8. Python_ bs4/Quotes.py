from requests import Session
from bs4 import BeautifulSoup
from time import sleep

url_quotes_toscrape = 'https://quotes.toscrape.com/'
url_login = 'https://quotes.toscrape.com/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://quotes.toscrape.com/login',
    'Connection': 'keep-alive',
    # 'Cookie': 'session=eyJjc3JmX3Rva2VuIjoiVmxjQ2FycEtocW1aRlVTUERNc3ZpV2V5YmpKemRmTE51Z09UeEl3RWtHUVluWEhCb3RSQSIsInVzZXJuYW1lIjoiQXphbCJ9.Z-Q5jw.vLVWaeCcXET8q5kYaucsA2w6eUM',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

work = Session()
work.get(url_quotes_toscrape, headers=headers)  # запрос для имитации захода на сайт без логирования
response = work.get(url_login, headers=headers)  # заходим на страницу авторизации

soup = BeautifulSoup(response.text, 'lxml')
token = soup.find("form").find("input").get("value")
print(token)
data = {
	"csrf_token": token,
	"username": "Azal",
	"password": "1234"
}

result = work.post(url_login, headers=headers, data=data, allow_redirects=True) # allow_redirects перенаправлние включино

print(result.text)

result = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')

# if len(result) != 0:

# else:
#     break