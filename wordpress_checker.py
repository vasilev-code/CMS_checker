import requests
from bs4 import BeautifulSoup
import re

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
b = soup.find(string=re.compile("wp-content"))
if "wp-content" in b:
    print("Yes")
else:
    print("No")