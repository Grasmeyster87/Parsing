from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import asyncio


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

page_arr = ['https://www.olx.ua/uk/transport/?page=1', 'https://www.olx.ua/uk/transport/?page=2',
            'https://www.olx.ua/uk/transport/?page=3', 'https://www.olx.ua/uk/transport/?page=4',
            'https://www.olx.ua/uk/transport/?page=5']  # массив ссылок

num_tabs = 2 # количество вкладов одновременно открываемых


async def get_cards_sync(page_arr, num_tabs):
    # Открываем недостающие вкладки
    for _ in range(num_tabs - 1):
        driver.execute_script("window.open('', '_blank');")
    await asyncio.sleep(2)

    tabs = driver.window_handles  # Обновляем список вкладок

    tab_index = 0  # Указатель на текущую вкладку

    while page_arr:
        driver.switch_to.window(tabs[tab_index])
        url = page_arr.pop(0)
        print(f"Вкладка {tab_index} -> {url}")
        driver.get(url)

        # Переход к следующей вкладке по кругу
        tab_index = (tab_index + 1) % num_tabs

        await asyncio.sleep(3)  # Пауза между загрузками


def make_page(page_arr, num_tabs):
    asyncio.run(get_cards_sync(page_arr, num_tabs))


make_page(page_arr, num_tabs)