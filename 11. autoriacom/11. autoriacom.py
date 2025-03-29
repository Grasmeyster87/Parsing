import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://auto.ria.com/uk/search/?indexName=auto&plateNumber.length.gte=1&body.id[0]=3&year[0].gte=2015&categories.main.id=1&brand.id[0]=24&country.origin.id[0]=840&country.import.usa.not=-1&price.USD.lte=20000&price.currency=1&mileage.lte=100000&engine.gte=1&abroad.not=0&custom.not=1&power.hp.gte=150&page=0&size=1000',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.2100364150.1742975485; _ga_BD9ZHFE1XX=GS1.1.1743154933.4.1.1743155099.0.0.0',
}

# URL page
url = 'https://auto.ria.com/uk/search/?indexName=auto&plateNumber.length.gte=1&body.id[0]=3&year[0].gte=2015&categories.main.id=1&brand.id[0]=24&country.origin.id[0]=840&country.import.usa.not=-1&price.USD.lte=20000&price.currency=1&mileage.lte=100000&engine.gte=1&abroad.not=0&custom.not=1&power.hp.gte=150&page=0&size=1000'

# Download page
response = requests.get(url, headers=headers)
# print(response.raise_for_status())
# print(response.status_code)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')

# Получаем карточку автомобиля

car_cards = soup.find_all("section", class_='ticket-item')

# Здесь будут данные всех автомобилей
cars = []

# Цикл для прохождения по всем карточкам с дальнейшей обработкой
for car_card in car_cards:
    car_data = {}

    # Название автомобиля
    title_name = car_card.find('a', class_='address').text
    link = car_card.find('a', class_='address').get('href')
    
    if title_name:
        car_data['title'] = title_name
        car_data['link'] = link
    print(car_data)

    # добавляем данные автомобиля в массив
    cars.append(car_data)

# Запишем все данные в CSV файл

with open('cars.csv', mode='w', newline='', encoding='utf-8') as file:
    # fildnames = ['title', 'link', 'mileage', 'year', 'location', 'photo_link', 'date_posted']
    fildnames = ['title', 'link']
    writer = csv.DictWriter(file, fieldnames=fildnames)
    writer.writeheader()

    for car in cars:
        writer.writerow(car)