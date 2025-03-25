cURL_DNS = 'curl "https://www.dns-shop.ru/search/?q=dbltjrfhns&category=17a89aab16404e77" --compressed -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: https://www.dns-shop.ru/" -H "Connection: keep-alive" -H "Cookie: _ga_ND7GY87YET=GS1.1.1740916845.8.1.1740917520.60.0.1576000873; _ga=GA1.1.189348714.1728410175; qrator_ssid=1742914560.419.ZSwJRXzZDjdgeExc-gbprjsh8hpn8omfresd230e73ai3upv3; qrator_jsid=1742914560.087.1ohJfOhL00Lg1ROF-3q69jhbrtedajvhp63g2g440aeoiqcps; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A12^%^3A^%^22current_path^%^22^%^3Bi^%^3A1^%^3Bs^%^3A116^%^3A^%^22^%^7B^%^22city^%^22^%^3A^%^2230b7c1f3-03fb-11dc-95ee-00151716f9f5^%^22^%^2C^%^22cityName^%^22^%^3A^%^22^%^5Cu041c^%^5Cu043e^%^5Cu0441^%^5Cu043a^%^5Cu0432^%^5Cu0430^%^22^%^2C^%^22method^%^22^%^3A^%^22default^%^22^%^7D^%^22^%^3B^%^7D; lang=ru; city_path=moscow; PHPSESSID=2ee16fb6fd5834909f51ce4c8090413c; _csrf=e63362fc25472f9a219b03bdf7141c45c7e47355ff9ca41a84b7ff8c6b009a61a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^2203gQu1ZA8qYWjssyYe4zo22uXoDPO4AX^%^22^%^3B^%^7D; cartUserCookieIdent_v3=5e2fa7142764818cffffbc43ebd8a21b91b013b64c813d9b7440adb9e899e59fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22cartUserCookieIdent_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A36^%^3A^%^220de4c336-ca7a-3876-81d4-86e9faf8382c^%^22^%^3B^%^7D; qrator_jsr=1742914560.087.1ohJfOhL00Lg1ROF-6m07ariskrep4l6lm3h020utt846dhg5-00" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Priority: u=0, i" -H "Pragma: no-cache" -H "Cache-Control: no-cache"'

from curl_fetch2py import CurlFetch2Py
import requests

cookies = {
    '_ga_ND7GY87YET': 'GS1.1.1740916845.8.1.1740917520.60.0.1576000873',
    '_ga': 'GA1.1.189348714.1728410175',
    'qrator_ssid': '1742914560.419.ZSwJRXzZDjdgeExc-gbprjsh8hpn8omfresd230e73ai3upv3',
    'qrator_jsid': '1742914560.087.1ohJfOhL00Lg1ROF-3q69jhbrtedajvhp63g2g440aeoiqcps',
    'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A12^%^3A^%^22current_path^%^22^%^3Bi^%^3A1^%^3Bs^%^3A116^%^3A^%^22^%^7B^%^22city^%^22^%^3A^%^2230b7c1f3-03fb-11dc-95ee-00151716f9f5^%^22^%^2C^%^22cityName^%^22^%^3A^%^22^%^5Cu041c^%^5Cu043e^%^5Cu0441^%^5Cu043a^%^5Cu0432^%^5Cu0430^%^22^%^2C^%^22method^%^22^%^3A^%^22default^%^22^%^7D^%^22^%^3B^%^7D',
    'lang': 'ru',
    'city_path': 'moscow',
    'PHPSESSID': '2ee16fb6fd5834909f51ce4c8090413c',
    '_csrf': 'e63362fc25472f9a219b03bdf7141c45c7e47355ff9ca41a84b7ff8c6b009a61a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^2203gQu1ZA8qYWjssyYe4zo22uXoDPO4AX^%^22^%^3B^%^7D',
    'cartUserCookieIdent_v3': '5e2fa7142764818cffffbc43ebd8a21b91b013b64c813d9b7440adb9e899e59fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22cartUserCookieIdent_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A36^%^3A^%^220de4c336-ca7a-3876-81d4-86e9faf8382c^%^22^%^3B^%^7D',
    'qrator_jsr': '1742914560.087.1ohJfOhL00Lg1ROF-6m07ariskrep4l6lm3h020utt846dhg5-00',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.dns-shop.ru/',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga_ND7GY87YET=GS1.1.1740916845.8.1.1740917520.60.0.1576000873; _ga=GA1.1.189348714.1728410175; qrator_ssid=1742914560.419.ZSwJRXzZDjdgeExc-gbprjsh8hpn8omfresd230e73ai3upv3; qrator_jsid=1742914560.087.1ohJfOhL00Lg1ROF-3q69jhbrtedajvhp63g2g440aeoiqcps; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A12^%^3A^%^22current_path^%^22^%^3Bi^%^3A1^%^3Bs^%^3A116^%^3A^%^22^%^7B^%^22city^%^22^%^3A^%^2230b7c1f3-03fb-11dc-95ee-00151716f9f5^%^22^%^2C^%^22cityName^%^22^%^3A^%^22^%^5Cu041c^%^5Cu043e^%^5Cu0441^%^5Cu043a^%^5Cu0432^%^5Cu0430^%^22^%^2C^%^22method^%^22^%^3A^%^22default^%^22^%^7D^%^22^%^3B^%^7D; lang=ru; city_path=moscow; PHPSESSID=2ee16fb6fd5834909f51ce4c8090413c; _csrf=e63362fc25472f9a219b03bdf7141c45c7e47355ff9ca41a84b7ff8c6b009a61a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^2203gQu1ZA8qYWjssyYe4zo22uXoDPO4AX^%^22^%^3B^%^7D; cartUserCookieIdent_v3=5e2fa7142764818cffffbc43ebd8a21b91b013b64c813d9b7440adb9e899e59fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22cartUserCookieIdent_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A36^%^3A^%^220de4c336-ca7a-3876-81d4-86e9faf8382c^%^22^%^3B^%^7D; qrator_jsr=1742914560.087.1ohJfOhL00Lg1ROF-6m07ariskrep4l6lm3h020utt846dhg5-00',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0, i',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'q': 'dbltjrfhns',
    'category': '17a89aab16404e77',
}

response = requests.get('https://www.dns-shop.ru/search/', params=params, cookies=cookies, headers=headers)

with open('result.html', 'w') as file:
    file.write(response.text)


context_curl = CurlFetch2Py.parse_curl_context(cURL_DNS)


request_curl = requests.get(url=context_curl.url,
                            headers=context_curl.headers,
                            cookies=context_curl.cookies)


with open('result_curl.html', 'w', encoding='utf-8') as result:
    result.write(request_curl.text)