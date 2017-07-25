import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_phone_number(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        data = soup.find('span', class_='opencontact').text.strip()
    except:
        data = ''
    return data
