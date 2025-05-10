from moduls.put_data_card import put_data_card
from moduls.db_OLX import OLX_cars_db, DB_NAME
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import time

from moduls.CONSTANTS import num_tabs, user_id, limit

import colorama
from colorama import Fore, Back, Style
colorama.init()


def create_driver(user_id=1):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=0")
    # options.add_argument("--disable-gpu")
    options.add_argument("----enable-unsafe-swiftshader")

    # Указываем нужную директорию с профилем
    script_dir = os.path.dirname(os.path.abspath(__file__))
    user_dir = os.path.join(script_dir, 'users', f'user_{user_id}')
    options.add_argument(f"user-data-dir={user_dir}")

    # Если нужно создать директорию, если её нет
    os.makedirs(user_dir, exist_ok=True)

    driver = webdriver.Chrome(options=options)
    stealth(driver,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win64",  # Изменено с Win32 на Win64
            webgl_vendor="Nvidia Corporation",  # Изменено с Intel Inc.
            renderer="Nvidia GeForce 4060TI",  # Изменено с Intel Iris OpenGL Engine
            fix_hairline=True
            )
    driver.implicitly_wait(5)  # задержка ожидания по умолчанию
    return driver


# driver = create_driver(user_id)

# page_arr = OLX_cars_db.get_DB_OLX_link_cards(DB_NAME, limit)


def get_card_sync(driver, page_arr, num_tabs):
    # Открываем недостающие вкладки
    for _ in range(num_tabs - 1):
        driver.execute_script("window.open('', '_blank');")
    time.sleep(2)

    tabs = driver.window_handles  # Обновляем список вкладок

    tab_index = 0  # Указатель на текущую вкладку

    data = []
    kol_elem_v_mas = len(page_arr)
    while page_arr:
        driver.switch_to.window(tabs[tab_index])

        if page_arr:
            olx_cards_id, url = page_arr.pop(0)

        print(
            f"{Fore.CYAN}Вкладка {tab_index}{Style.RESET_ALL} ({Fore.MAGENTA}{len(page_arr)} из {kol_elem_v_mas}{Style.RESET_ALL})  -> {Fore.CYAN}{url}{Style.RESET_ALL}")
        driver.get(url)
        # -------------------------------------- get data
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-10ofhqw"))
            )
            try:
                title = driver.find_element(By.CLASS_NAME, "css-10ofhqw").text
            except:
                title = "Нет названия"

            try:
                price = driver.find_element(By.CLASS_NAME, "css-fqcbii").text
            except:
                price = "Цена не указана"

            try:
                user = driver.find_element(By.CLASS_NAME, "css-1titsw2").text
            except:
                user = "Пользователь не указан"

            try:
                description = driver.find_element(
                    By.CLASS_NAME, "css-19duwlz").text
            except:
                description = "Нет описания"

            data.append({"title": title, "price": price,
                        "user": user, "description": description, "olx_cards_id": olx_cards_id, })

        except Exception as e:
            # print(f"Ошибка при загрузке страницы: {e}")
            print(Fore.GREEN + "Ошибка при загрузке страницы" + Style.RESET_ALL)
            data.append({"title": 'NULL', "price": 'NULL',
                        "user": 'NULL', "description": 'NULL', "olx_cards_id": olx_cards_id, })
            # return []
            continue

        finally:
            time.sleep(3)
        # --------------------------------------
        # Переход к следующей вкладке по кругу
        tab_index = (tab_index + 1) % num_tabs
        time.sleep(3)  # Пауза между загрузками

    # num = 1
    # for card in data:
    #     print(num, card, '\n')
    #     num += 1
    return data



# def page_processing(page_arr, num_tabs):
#     return get_card_sync(page_arr, num_tabs)


# data = page_processing(page_arr, num_tabs)
# put_data_card(data)
# OLX_cars_db.delete_DB_OLX_null_cards(DB_NAME_MODULS)
