import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.google.com/search?q=%D0%BA%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%B5%D1%80+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&oq=%D0%BA%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82+%D0%B3%D1%80%D0%B8&aqs=chrome.1.69i57j0l5.6960j1j7&sourceid=chrome&ie=UTF-8'
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
def check_currency():
    full_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 3 })
    print("Сейчас курс: 1 гривна = " + convert[0].text)
    time.sleep(3)
    check_currency()

check_currency()
