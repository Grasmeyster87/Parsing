from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import asyncio

from db_OLX import OLX_cars_db, DB_NAME, DB_NAME_MODULS


def create_driver(user_id=1):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # options.add_argument('--headless')
    # Запускает браузер в безголовом режиме (без графического интерфейса, фоном), что полезно для автоматизации и тестирования. С этим аргументом бывают интересные штуки. Иногда драйвер начинает работать быстрее, многда медленнее, а иногда и вовсе сайт это вычисляет и закрывает доступ брузеру. Так что с этим будьте аккуратны. На примере аргумент закомментирован.

    script_dir = os.path.dirname(os.path.abspath(__file__))
    user_dir = os.path.join(script_dir, 'users', f'user_{user_id}')
    options.add_argument(f'user-data-dir={user_dir}')
    # options.add_argument('--disable-gpu')
    options.add_argument('--enable-unsafe-webgpu')
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')  # включить при необходимости

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

driver = create_driver(user_id=1)

num_tabs = 2  # количество вкладов одновременно открываемых

page_arr = OLX_cars_db.get_DB_OLX_link_cards(DB_NAME_MODULS)


async def get_cards_sync(page_arr, num_tabs):
    # Открываем недостающие вкладки
    for _ in range(num_tabs - 1):
        driver.execute_script("window.open('', '_blank');")
    await asyncio.sleep(2)

    tabs = driver.window_handles  # Обновляем список вкладок

    tab_index = 0  # Указатель на текущую вкладку

    data = []
    while page_arr:
        driver.switch_to.window(tabs[tab_index])

        if page_arr:
            olx_cards_id, url = page_arr.pop(0)

        print(f"Вкладка {tab_index} -> {url}")
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
            print(f"Ошибка при загрузке страницы: {e}")
            data.append({"title": 'NULL', "price": 'NULL',
                        "user": 'NULL', "description": 'NULL', "olx_cards_id": olx_cards_id, })
            # return []
            continue


        finally:
            await asyncio.sleep(3)
        # --------------------------------------
        # Переход к следующей вкладке по кругу
        tab_index = (tab_index + 1) % num_tabs
        await asyncio.sleep(3)  # Пауза между загрузками

    num = 1
    for card in data:
        print(num, card, '\n')
        num += 1
    return data


def put_data_card(cards):
    """Обрабатывает карточки и сохраняет их в базу данных"""
    for card in cards:
        try:
            title = card.get("title", "Нет названия")
            price = card.get("price", "Нет цены")
            # будет сохраняться в поле "link"
            user = card.get("user", "Нет ссылки")
            description = card.get("description", "Нет ссылки")
            olx_cards_id = card.get("olx_cards_id", "Нет ссылки")

            OLX_cars_db.save_card(title=title, price=price,
                                  user=user, description=description, olx_cards_id = olx_cards_id)

        except Exception as e:
            print(f"Ошибка при обработке данных: {e}")


def page_processing(page_arr, num_tabs):
    return asyncio.run(get_cards_sync(page_arr, num_tabs))

data = page_processing(page_arr, num_tabs)
put_data_card(data)
