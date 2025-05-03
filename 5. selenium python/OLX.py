from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sqlite3

# import from moduls
from moduls.save_to_html import save_to_html
from moduls.output_result import output_result
from moduls.db_OLX import OLX_cars_db, DB_NAME

# Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализация драйвера браузера.
driver = webdriver.Chrome()

# установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
time.sleep(3)

# С помощью метода GET мы скажем браузеру, что надо открыть
number = 1
number_max = 25

driver.get(f"https://www.olx.ua/uk/transport/?page={number}")

time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "css-qfzx1y"))
)
# cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")

# Ищем все элементы <a> с нужным классом
cards_link = driver.find_elements(By.CLASS_NAME, "css-1tqlkj0")
# Получаем атрибут href из каждого найденного элемента
hrefs = [link.get_attribute("href") for link in cards_link]


# Ищем все элементы <h4> с нужным классом
cards_title = driver.find_elements(By.CLASS_NAME, "css-1g61gc2")
# Получаем атрибут titles из каждого найденного элемента
titles = [title.text for title in cards_title]


cards_price = driver.find_elements(By.CLASS_NAME, "css-uj7mm0")
price = [price.text for price in cards_price]

cards_place_date = driver.find_elements(By.CLASS_NAME, "css-vbz67q")
places_dates = [place_date.text for place_date in cards_place_date]

# Создаем массив cards, объединяя заголовки и ссылки
cards = [{'title': title, 'link': href, 'price': price, 'place_date': place_date}
         for title, href, price, place_date in zip(titles, hrefs, price, places_dates)]


OLX_cars_db.create_db(DB_NAME)
OLX_cars_db.create_new_table_olx_cards(DB_NAME)
OLX_cars_db.create_new_table_olx_card(DB_NAME)
OLX_cars_db.create_new_strings(DB_NAME, cards)
# OLX_cars_db.create_new_strings(DB_NAME, courses)

# OLX_cars_db.read_DB(DB_NAME)

# Выводим полученные ссылки
num = 1
for card in cards:
    print(num, card, '\n\n')
    num = num + 1

# output_result(cards_link)
# output_result(cards)

# save_to_html(cards)

driver.quit()
