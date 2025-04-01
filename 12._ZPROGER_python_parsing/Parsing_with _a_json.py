import json
import requests
from bs4 import BeautifulSoup

# Сайт недоступен код набран для примера
def get_js(sp):
    block = sp.find('div', id='javascript_check')
    return block.find_all('span')[1].text


def get_cookie(sp):
    block = sp.find('div', id='cookie_check')
    return block.find_all('span')[1].text


def get_flash(sp):
    block = sp.find('div', id='flash_version')
    return block.find_all('span')[1].text

def main():
    with open('config.json') as file:
        config = json.load(file)

    response = requests.get('https://browser-info.ru/')
    soup = BeautifulSoup(response, 'lxml')

    print(response.text)

    print(get_js(soup))
    print(get_cookie(soup))
    print(get_flash(soup))

    if config['js'] == True: get_js(soup)
    if config['cookie'] == True: get_cookie(soup)
    if config['flash'] == True: get_flash(soup)

if __name__ == '__main__':
    main()