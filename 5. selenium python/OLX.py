from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# import from moduls
from moduls.save_to_html import save_to_html

# Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализация драйвера браузера.
driver = webdriver.Chrome()

# установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
time.sleep(5)

# С помощью метода GET мы скажем браузеру, что надо открыть
number = 1
number_max = 25

driver.get(f"https://www.olx.ua/uk/transport/?page={number}")

time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "css-l9drzq"))
)
cards = driver.find_elements(By.CLASS_NAME, "css-l9drzq")



save_to_html(cards)


driver.quit()
