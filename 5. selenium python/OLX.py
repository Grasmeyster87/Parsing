# Webdriver - это и есть набор команд для управления браузером
# pip install selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# pipenv install selenium-stealth
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
# pipenv install fake-useragent
from fake_useragent import UserAgent

import time
import sqlite3
import os

# import from moduls
from moduls.save_to_html import save_to_html
from moduls.output_result import output_result
from moduls.db_OLX import OLX_cars_db, DB_NAME

number_max = 3


def get_cards(number_max):
    # инициализация драйвера браузера.
    driver = webdriver.Chrome()

    # установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
    time.sleep(5)

    OLX_cars_db.create_db(DB_NAME)
    OLX_cars_db.create_new_table_olx_cards(DB_NAME)
    OLX_cars_db.create_new_table_olx_card(DB_NAME)

    # С помощью метода GET мы скажем браузеру, что надо открыть
    number = 1
    for i in range(1, number_max):
        driver.get(f"https://www.olx.ua/uk/transport/?page={i}")
        print(f"parsing page cards №{i} is run")
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-qfzx1y"))
        )
        # cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")

        # Родительские элементы карточек
        cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")
        results = []
        for card in cards:
            title_element = card.find_element(
                By.CLASS_NAME, "css-1g61gc2")  # Заголовок
            link_element = card.find_element(
                By.CLASS_NAME, "css-1tqlkj0")  # Ссылка
            price_element = card.find_element(
                By.CLASS_NAME, "css-uj7mm0")  # Цена
            place_date_element = card.find_element(
                By.CLASS_NAME, "css-vbz67q")  # место и описание короткое

            title = title_element.text if title_element else "Нет заголовка"
            href = link_element.get_attribute(
                "href") if link_element else "Нет ссылки"
            price = price_element.text
            place_date = place_date_element.text
            parts = place_date.split(" - ")

            place = parts[0]
            date = parts[1]

            results.append({'title': title, 'link': href,
                           'price': price, 'place': place, 'date': date})

        OLX_cars_db.create_new_strings(DB_NAME, results)
        time.sleep(1)

    OLX_cars_db.create_index(DB_NAME)

    OLX_cars_db.remove_duplicates_olx_cards(DB_NAME)
    OLX_cars_db.remove_duplicates_olx_card(DB_NAME)

    # OLX_cars_db.read_DB_OLX_cards(DB_NAME)

    # output_result(cards_link)
    # output_result(cards)

    # save_to_html(cards)

    driver.quit()


if __name__ == '__main__':
    get_cards(number_max)
