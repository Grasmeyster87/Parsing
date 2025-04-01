import re               # библитека для регулярных выражений
import requests
import multiprocessing  # библиотке для мульти процессинга

# Код для примера адреса прокси старые
def handler(proxy):
    link = "http://icanhazip.com/"

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        responce = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {responce.strip()}')
    except:
        print('Прокси не валидный')


with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    process.map(handler, proxy_base)
