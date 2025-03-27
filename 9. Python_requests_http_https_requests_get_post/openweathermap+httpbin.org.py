import requests
from apikey import API_TOKEN
import json

# params = {"q": "Horishni Plavni", "appid": API_TOKEN, "units": "metric"}
data = {
	"custname": "Azal11",
	"custtel": "+380964082463",
	"custemail": "123@meta.ua",
	"size": "medium",
	"topping": [
		"bacon",
		"cheese",
		"onion",
		"mushroom"
	],
	"delivery": "",
	"comments": ""
}
# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Host": "httpbin.org",
    "Priority": "u=0",
    "Referer": "https://httpbin.org/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "X-Amzn-Trace-Id": "Root=1-67e5547a-0e1e2553322b0e6b4c6c4be9"
  }
# response = requests.get("https://httpbin.org/headers", headers=headers)

variable = requests.Session()

variable.get("https://httpbin.org/post")

response = variable.post("https://httpbin.org/post", headers=headers, data=data, allow_redirects=True)

# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)
# print(response.json())
# weather = response.json()
# print(weather["weather"][0]["main"])

print(response.text)

