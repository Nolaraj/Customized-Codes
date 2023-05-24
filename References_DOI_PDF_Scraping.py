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
import docx

#pip install requests parsel google-search-results
from parsel import Selector
import requests, json, os


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








folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads', "Research Papers")
file_name = os.path.join(folder, 'References.docx')

i = 2
url = 'https://scholar.google.com/'

url_0 = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="








doi = []
doc = docx.Document(file_name)
all_paras = doc.paragraphs
def replace(text):
    text = text.replace(' ', '+')
    text = text.replace('[', '')
    text = text.replace(']', '')


    text = text + "&btnG="
    return text


def extractor(query, sources):
    params = {
        "q": f'{query.lower()} {sources}',  # search query
        "hl": "en",  # language of the search
        "gl": "us"  # country of the search
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=30)
    selector = Selector(html.text)

    publications = []

    for result in selector.css(".gs_r.gs_scl"):
        title = result.css(".gs_rt").xpath("normalize-space()").get()
        link = result.css(".gs_rt a::attr(href)").get()
        result_id = result.attrib["data-cid"]
        snippet = result.css(".gs_rs::text").get()
        publication_info = result.css(".gs_a").xpath("normalize-space()").get()
        cite_by_link = f'https://scholar.google.com/scholar{result.css(".gs_or_btn.gs_nph+ a::attr(href)").get()}'
        all_versions_link = f'https://scholar.google.com/scholar{result.css("a~ a+ .gs_nph::attr(href)").get()}'
        related_articles_link = f'https://scholar.google.com/scholar{result.css("a:nth-child(4)::attr(href)").get()}'
        pdf_file_title = result.css(".gs_or_ggsm a").xpath("normalize-space()").get()
        pdf_file_link = result.css(".gs_or_ggsm a::attr(href)").get()


        publications.append({
        "result_id": result_id,
        "title": title,
        "link": link,
        "snippet": snippet,
        "publication_info": publication_info,
        "cite_by_link": cite_by_link,
        "all_versions_link": all_versions_link,
        "related_articles_link": related_articles_link,
        "pdf": {
            "title": pdf_file_title,
            "link": pdf_file_link
        }
    })

    # return publications

    print(json.dumps(publications, indent=2, ensure_ascii=False))


for para in all_paras:
    search =  para.text
    print(search)
    extractor(query = search, sources = [""])



