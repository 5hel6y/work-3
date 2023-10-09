import requests
from bs4 import BeautifulSoup
data = 'https://store.steampowered.com/genre/Free%20to%20Play/'
url = requests.get(data)
soup = BeautifulSoup(url.text, "html.parser")
all_link = {}
exception = "Fr"
tag, tag_2 = ('a href ='), ("class text/css")
for link in soup.find_all('a'):
 all_link[link.get('href')] = (link.text)
for key, value in all_link.items():
 print("{0}: {1}".format(key,value))

