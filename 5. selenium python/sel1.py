import time


#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


#инициализация драйвера браузера.
driver = webdriver.Chrome()


#установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
time.sleep(5)


#С помощью метода GET мы скажем браузеру, что надо открыть
driver.get("http://fortesters.easysmarthub.ru/form1/")
time.sleep(5)




#Метод  find_element позволяет найти нужный элемент на сайте.
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")


#питон за нас напишет текст get() в поле textarea
textarea.send_keys("get()")
time.sleep(5)


#найдем кнопку как в предыдущем случае
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")


#выполним действие нажатии на кнопку
submit_button.click()
time.sleep(5)


#После выполнения всех дейсвтий мы закрываем окно браузера.
driver.quit()


# chrome - тут https://www.google.com.sg/intl/en/chrome/



#  https://sites.google.com/chromium.org/driver/ - тут скачиваем гугл драйвер



# Идем на диск C: и тут создаем папку chromedriver


# Добавляем webdriver d path

# Проверяем работу через командную строку

# Бесплатный курс по питону  - https://easysmarthub.ru/courses/python-tajny-kotorye-vam-ne-rasskazhut-drugie-kursy/




# Локальное окружение python VS CODE

# Windows
# 1. Запустить VS Code от имени администратора, перейти в каталог проекта в PowerShell, выполнить код ниже, появится папка env, содержащая файлы виртуального окружения
# python -m venv env
# 2. Изменить политику, в PowerShell набрать
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 3. Войти в папку окружения (env), выполнить команду
# env\Scripts\activate.ps1
# env\Scripts\activate.bat