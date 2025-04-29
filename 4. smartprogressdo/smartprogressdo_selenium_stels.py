# pip install selenium selenium-stealth fake-useragent

import os
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import time

# Создаем функцию для генерации рандомного User-Agent:


def get_random_chrome_user_agent():
    user_agent = UserAgent(browsers='chrome', os='windows', platforms='pc')
    return user_agent.random

# Не забудьте создать папку users в корне вашего проекта!


def create_driver(user_id=1):
    # Здесь создается экземпляр класса Options, который используется для настройки поведения Chrome WebDriver.

    options = Options()
    # Добавляется аргумент для запуска браузера в режиме максимального окна.

    options.add_argument("start-maximized")
    # Добавляется экспериментальная опция, исключающая переключатель "enable-automation", чтобы предотвратить автоматическое обнаружение, что браузер управляется WebDriver.

    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
     # Добавляется экспериментальная опция, исключающая переключатель "enable-automation", чтобы предотвратить автоматическое обнаружение, что браузер управляется WebDriver.

    options.add_experimental_option('useAutomationExtension', False)
    # Добавляется экспериментальная опция, отключающая расширение автоматизации в браузере, что также помогает скрыть использование WebDriver.

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Эта строка получает абсолютный путь к текущему скрипту и извлекает директорию, в которой он находится. file содержит путь к текущему файлу.

    base_directory = os.path.join(script_dir, 'users')
    # Создается путь к базовой директории users, которая находится в той же директории, что и текущий скрипт. (если не находится - исправьте). В этой дирректории мы будем хранить папки с пользователями. Далее достаточно будет повторно указать айдишник пользователя и вы сможете «вернуться в профиль».

    user_directory = os.path.join(base_directory, f'user_{user_id}')
    # Создается путь к директории конкретного пользователя, используя значение user_id. Например, если user_id равно 1, будет создан путь users/user_1.


    options.add_argument(f'user-data-dir={user_directory}')
    # Добавляется аргумент для Chrome, указывающий на директорию с данными пользователя. Это позволяет использовать разные профили Chrome для разных пользователей.

    options.add_argument('--disable-gpu')
    # Отключается использование GPU в браузере. Это иногда необходимо для правильной работы в средах без графического интерфейса. Аргумент не обязательный, но можете с ним поиграться.

    options.add_argument('--disable-dev-shm-usage')
    # Отключается использование разделяемой памяти /dev/shm. Это может быть полезно для предотвращения проблем с памятью в контейнеризованных средах.

    options.add_argument("--disable-notifications")
    # Отключаются уведомления в браузере.

    options.add_argument("--disable-popup-blocking")
    # Отключается блокировка всплывающих окон.
    options.add_argument('--no-sandbox')
    # Отключается песочница (sandbox) для повышения стабильности в некоторых средах, но это уменьшает безопасность. Иногда без этого аргумента не запускается вебдрайвер на средах без GUI, но тоже указывать не обязательно.

    # options.add_argument('--headless')
    # Запускает браузер в безголовом режиме (без графического интерфейса, фоном), что полезно для автоматизации и тестирования. С этим аргументом бывают интересные штуки. Иногда драйвер начинает работать быстрее, многда медленнее, а иногда и вовсе сайт это вычисляет и закрывает доступ брузеру. Так что с этим будьте аккуратны. На примере аргумент закомментирован.


    driver = webdriver.Chrome(options=options)
    # Создается экземпляр WebDriver для Chrome с заданными параметрами options.

    ua = get_random_chrome_user_agent()
    # Получает случайный user-agent для Chrome. Это может быть функцией, которую мы написали выше или ваш собственный user-agent.

    stealth(driver=driver,
            user_agent=ua,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            run_on_insecure_origins=True
            )
    # Вызывает функцию stealth для маскировки использования WebDriver. Здесь устанавливаются различные параметры, такие как user_agent, languages, vendor, platform, webgl_vendor, renderer, и другие, чтобы сделать браузер менее распознаваемым как управляемый WebDriver.


    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
      '''
    })
    # Выполняет команду CDP (Chrome DevTools Protocol) для удаления определенных свойств из объекта window, которые могут использоваться для обнаружения WebDriver. К примеру с Озон вы не сможете работать без удаления этих свойств с объекта window.

    return driver


def main_login(user_id=1):
    driver = create_driver(user_id)
    driver.get('https://smartprogress.do/')

    expiriens = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'user-menu__info-text.user-menu__info-text--exp'))
    ).text

    print(expiriens)

    print(expiriens)
    time.sleep(350)


if __name__ == "__main__":
    main_login(user_id=1)