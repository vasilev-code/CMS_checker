import requests
from bs4 import BeautifulSoup
import re

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
wordpress = soup.find(string=re.compile("wp-content"))

def joomla(content):
    return content and re.compile("Joomla").search(content)
joomla_var = soup.find_all(content=joomla)

if joomla_var:
    print("Этот сайт разработан на движке Joomla")

else:
    try:
        if "wp-content" in wordpress:
            print("Этот сайт разработан на движке WordPress")

    except TypeError:
        print("Движок неизвестен")
        