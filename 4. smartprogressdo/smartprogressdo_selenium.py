from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options # загрузка браузера с профилем
import time


# загрузка браузера с профилем
options = Options()
options.add_argument('-profile')
options.add_argument('C:\Users\Azal\AppData\Local\Mozilla\Firefox\Profiles\0ulk4ury.default')

# URL для входа
ligin_url = 'https://smartprogress.do/user/login/'
driver = webdriver.Firefox(options=options,
                           executable_path='geckodriver.exe',
                           service_args=['--marionette-port', '2828'])
driver.get(ligin_url)

# Ожидание загрузки полей ввода
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#UserLoginForm_email"))
)

# Заполнение полей
UserLoginForm_email = driver.find_element(
    By.CSS_SELECTOR, "#UserLoginForm_email")
UserLoginForm_password = driver.find_element(
    By.CSS_SELECTOR, "#UserLoginForm_password")

UserLoginForm_email.send_keys("azal11@meta.ua")
UserLoginForm_password.send_keys("[Azal_job11]")

# Ожидание загрузки iframe
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src*='recaptcha']"))
)

# Ожидание и клик по чекбоксу reCAPTCHA
recaptcha_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
)
recaptcha_checkbox.click()

# Возвращение в основное окно
driver.switch_to.default_content()

# Нахождение кнопки "Войти"
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.user-form__submit.btn.btn_theme_blue"))
)

# Клик по кнопке
submit_button.click()


# Время для наблюдения
time.sleep(100)

# Закрытие браузера
driver.quit()