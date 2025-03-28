import requests

url_ajaxdetail = 'https://scrapingclub.com/exercise/ajaxdetail/'

response = requests.get(url_ajaxdetail).json()


print(response['title'])
print(response['price'])
print(response['description'])
print(response)