import requests
key = 'fa55c9b48bf19b93b69b0f2b81fdf56c'
url = 'https://api.openweathermap.org/data/2.5/weather'
city = (input("Введите город на английском\n"))
payload = {'q': 'city', 'appid': key}
result = requests.get(url, params=payload)
print(result.content)
