from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import time


def create_driver(user_id=1):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
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
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
            )
    driver.implicitly_wait(5)  # задержка ожидания по умолчанию
    return driver


def get_cards_sync(page_number, user_id):
    driver = create_driver(user_id)
    driver.get(f"https://www.olx.ua/uk/transport/?page={page_number}")
    print(f"Загрузка страницы №{page_number}")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-qfzx1y"))
        )
        cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")
        data = []

        for card in cards:
            try:
                title = card.find_element(By.CLASS_NAME, "css-1g61gc2").text
            except:
                title = "Нет названия"

            try:
                price = card.find_element(By.CLASS_NAME, "css-uj7mm0").text
            except:
                price = "Цена не указана"

            try:
                url = card.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                url = "Нет ссылки"
            try:
                place_date_element = card.find_element(
                    By.CLASS_NAME, "css-vbz67q").text
                parts = place_date_element.split(" - ")
                place = parts[0]
                date = parts[1]
            except:
                place = "Нет места или даты"

            data.append({"title": title, "price": price,
                        "url": url, "place": place, "date": date})

        return data

    except Exception as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []

    finally:
        time.sleep(2)
        driver.quit()
