import requests
from bs4 import BeautifulSoup as BS
import fake_useragent
from colorama import init, Fore, Style

# Инициализируем colorama для красивых принтов
init(autoreset=True)

# Параметры
LOGIN = "azal11@meta.ua"
PASSWORD = "[Azal_job11]"
BASE_URL = "https://smartprogress.do/"

# Функция для печати статусов
def print_status(message, status="info"):
    if status == "success":
        print(Fore.GREEN + "[+] " + message)
    elif status == "error":
        print(Fore.RED + "[-] " + message)
    else:
        print(Fore.CYAN + "[*] " + message)

# Функция для сохранения страницы
def save_html(page_name, content):
    with open(f"{page_name}.html", "w", encoding="utf-8") as file:
        file.write(str(content))
        print_status(f"Данные сохранены в файл {page_name}.html", "success")

def main():
    # Сессия
    s = requests.Session()

    # Заголовки
    user_agent = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Origin': BASE_URL,
        'Referer': BASE_URL,
        'Connection': 'keep-alive'
    }
    s.headers.update(headers)

    try:
        # 1. Получаем страницу для CSRF токена
        auth_html = s.get(BASE_URL)
        auth_html.raise_for_status()
        print_status("Главная страница загружена")

        auth_bs = BS(auth_html.content, 'html.parser')
        csrf_input = auth_bs.find('input', {'name': 'YII_CSRF_TOKEN'})
        
        if not csrf_input:
            print_status("Не найден CSRF токен на главной странице", "error")
            return
        
        csrf_token = csrf_input.get('value')
        print_status(f"Найден CSRF токен: {csrf_token}", "success")

        # 2. Выполняем логин
        payload = {
            "YII_CSRF_TOKEN": csrf_token,
            "returnUrl": '/',
            "UserLoginForm[email]": LOGIN,
            "UserLoginForm[password]": PASSWORD,
            "UserLoginForm[rememberMe]": 1
        }
        login_url = BASE_URL + "user/login"
        login_response = s.post(login_url, data=payload)
        login_response.raise_for_status()

        if "Неверный email или пароль" in login_response.text:
            print_status("Ошибка логина: неверные данные", "error")
            return
        
        print_status("Успешный вход на сайт", "success")

        # 3. Получаем сообщения
        unread_url = BASE_URL + "message/getUnread"
        unread_response = s.get(unread_url)
        unread_response.raise_for_status()
        print_status("Сообщения успешно получены", "success")
        print(unread_response)
        # 4. Сохраняем страницу
        save_html("messages", unread_response.text)

    except requests.RequestException as e:
        print_status(f"Ошибка HTTP запроса: {e}", "error")
    except Exception as e:
        print_status(f"Другая ошибка: {e}", "error")

if __name__ == "__main__":
    main()