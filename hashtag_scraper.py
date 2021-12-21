from bs4 import BeautifulSoup
import requests

headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
tiktok = requests.get('https://blog.hootsuite.com/tiktok-hashtags/', headers=headers)
soup = BeautifulSoup(tiktok.content, 'html.parser')
span = soup.find_all('li')
for x in range(len(span)):
    print(span[x].get_text())

