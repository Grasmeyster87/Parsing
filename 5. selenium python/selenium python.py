# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv

import os
username = os.getenv('username')
password = os.getenv('password')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # dopolnitelno

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")

# WebDriverWait(driver, 5).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
# )

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

ligin_url = 'https://detmir.market/login'
driver = webdriver.Firefox()
driver.get(ligin_url)

login_element = driver.find_element(By.NAME, "email")
login_element.clear()
login_element.send_keys("pycon")

password_element = driver.find_element(By.NAME, "password")
password_element.clear()
password_element.send_keys("username")
password_element.send_keys(Keys.RETURN)


driver.find_element(By.CSS_SELECTOR, "button[role='button']")

report_url = 'https://detmir.market/vendor/reports/reports'
driver.get(report_url)

# извлечь статистику
stats_table = driver.find_element(By.ID, 'detmir/scopes/table-1')

tabel_header = stats_table.find_element(By.CLASS_NAME, 'TableHeader__StyledTableHeader-sc-f7lu2u-sc-f7lu2u0')
table_columns = tabel_header.text.split('\n')

table_rows = stats_table.find_elements(By.CLASS_NAME, 'TableHeader__StyledTableHeader-sc-f7lu2u-sc-f7lu2u0')
table_data = [r.text.split('\n') for r in table_rows]

driver.close()