import requests
import fake_useragent
from bs4 import BeautifulSoup
from requests import Session
import os
from pathlib import *

image_path = WindowsPath('d:/image/')

image_number = 1
storage_number = 1
for storage in range(190):
    link = f"https://wallpaperscraft.ru/catalog/textures/1920x1080/page{storage_number}"
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    all_image = soup.find_all('li', class_='wallpapers__item')

    # info = all_image.find_all("span", class_="wallpapers__info")
    # print(info)

    for image in all_image:
        link_image = 'https://wallpaperscraft.ru' + image.find("a").get('href')
        link_text = image.find_all("span", class_="wallpapers__info")[-1].text
        # print('\n\n', link_image, '\t', link_text)
        # print(link_text, '\t')

        # Переходим на страницу и для сккачивания оригинала картинки
        download_storage = requests.get(link_image).text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        get_origin_link_img = download_soup.find("a", class_="gui-button gui-button_full-height").get("href")
        print(get_origin_link_img, ' ', link_text)

        # Download image
        image_bytes = requests.get(get_origin_link_img).content

        with open(f"{image_path}/{image_number} {link_text}.jpg", 'wb') as file:
            file.write(image_bytes)

        image_number += 1
        print(f"\nИзображение {image_number} {link_text}.jpg успешно скачано !\n\n")
    
    storage_number += 1