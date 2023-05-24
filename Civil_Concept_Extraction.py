import openpyxl as op
from time import sleep
import requests
import cloudscraper
import re
from bs4 import BeautifulSoup
import os
from selenium import webdriver

from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import shutil
import time
import random

def Soup_Extractor(url):
    scraper = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0', })
    response = scraper.get(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    session = requests.Session()
    response = session.get(url, headers=headers)

    content = response.content



    soup = BeautifulSoup(content, 'html.parser')

    return(soup)








folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')



i = 2
url = 'http://www.shipbucket.com/drawings?category=real'

url_0 = "https://www.civilconcept.com"

soup = Soup_Extractor(url_0)




# Finding the location of button
btn = soup.find("button", {"value": "Calculate"})

# Obtaining the text stored inside button tag
btn_text = btn.text

# Obtaining the onclick link of button tag
btn_onclick = btn['onclick']

# Printing the values
print(btn_text)
print(btn_onclick)









for tag in soup.find_all('a'):
    text_0 = tag.text.strip()
    texts = text_0.split(" ")
    text_0 = text_0 + ".png"

    for text in texts:
        if text in name:  # Checks for element with required name to provide url link and image link
            url3 = url_0 + tag['href']
            file_link = url_0 + tag.find('img')['src']

            # Downloading images from the site
            path = os.path.join(folder, text_0)
            r = requests.get(file_link, stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)




