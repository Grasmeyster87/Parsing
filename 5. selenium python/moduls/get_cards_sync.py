from moduls.CONSTANTS import user_id, num_tabs, number_max, memory_cards
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import time

import colorama
from colorama import Fore, Back, Style
colorama.init()


def create_driver():
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=0")

    driver = webdriver.Chrome(options=options)

    stealth(driver,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Nvidia Corporation",
            renderer="Nvidia GeForce 4060TI",
            fix_hairline=True
            )

    driver.implicitly_wait(5)
    return driver


def get_cards_sync_2(driver, number_max, num_tabs, memory_cards):
    for _ in range(num_tabs - 1):
        driver.execute_script("window.open('', '_blank');")
    time.sleep(2)

    tabs = driver.window_handles  # Обновляем список вкладок
    tab_index = 0  # Указатель на текущую вкладку

    data_cards_sync_2 = []
    kol_stranic = number_max

    while memory_cards <= number_max:
        driver.switch_to.window(tabs[tab_index])

        url = f"https://www.olx.ua/uk/transport/?page={memory_cards}"

        print(
            f"{Fore.CYAN}Вкладка {tab_index}{Style.RESET_ALL} ({Fore.MAGENTA}{memory_cards} из {kol_stranic}{Style.RESET_ALL})  -> {Fore.CYAN}{url}{Style.RESET_ALL}")
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-qfzx1y"))
            )
            cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")

            for card in cards:
                try:
                    title = card.find_element(
                        By.CLASS_NAME, "css-1g61gc2").text
                except:
                    title = "Нет названия"

                try:
                    price = card.find_element(By.CLASS_NAME, "css-uj7mm0").text
                except:
                    price = "Цена не указана"

                try:
                    card_url = card.find_element(
                        By.TAG_NAME, "a").get_attribute("href")
                except:
                    card_url = "Нет ссылки"
                try:
                    place_date_element = card.find_element(
                        By.CLASS_NAME, "css-vbz67q").text
                    parts = place_date_element.split(" - ")
                    place = parts[0]
                    date = parts[1]
                except:
                    place = "Нет места или даты"
                    date = ""

                data_cards_sync_2.append({"title": title, "price": price,
                                          "url": card_url, "place": place, "date": date})

        except Exception as e:
            print(f"Ошибка при загрузке страницы: {e}")

        tab_index = (tab_index + 1) % num_tabs
        memory_cards += 1
        time.sleep(5)

    driver.quit()
    # for i in data:
    #     print(i)
    return data_cards_sync_2


# get_cards_sync_2(number_max, num_tabs, memory_cards)
