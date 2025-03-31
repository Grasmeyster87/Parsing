import requests
import fake_useragent
from bs4 import BeautifulSoup
from requests import Session

# Session
# Authorization
# Get/Set cookies

# https://ru-forum.com/
# lesson_test:oA9h768p

user = fake_useragent.UserAgent().random

link = 'https://rutracker.net/forum/profile.php?mode=viewprofile&u=33028101'
link1 = 'https://rutracker.net/forum/login.php'


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://rutracker.net',
    'priority': 'u=0, i',
    'referer': 'https://rutracker.net/forum/index.php',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
    # 'cookie': 'bb_guid=QbCI6y6qxX4E',
}

data = {
    'login_username': 'Azal87',
    'login_password': 'Z82gf'
}

s = Session()
s.headers.update(headers)

response = s.post(link1, headers=headers, data=data)

profile_response = s.get(link, headers=headers)
soup = BeautifulSoup(profile_response.text, 'lxml')
prof_name = soup.find('h1', class_='pagetitle').text
print(prof_name)

# cookies_dict = [
#     {"domain": key.domain, "name": key.name, "path": key.path, "value":key.value}
#     for key in session.cookies:
# ]
# session2 = requests.Session()

# for cookies in cookies_dict:
#     session2.cookies.set(**cookies)

# resp = session2.get(link, headers=headers)
# print(resp.text)
