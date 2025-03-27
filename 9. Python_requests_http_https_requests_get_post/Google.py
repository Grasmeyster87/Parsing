import requests
params = {"q": "funny cats"}
response = requests.get("https://www.google.com/search", params=params)
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)
