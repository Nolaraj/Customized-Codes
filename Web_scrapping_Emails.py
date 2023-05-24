from time import sleep
import requests
import cloudscraper
import re
from bs4 import BeautifulSoup


emails = set()

def Soup_Extractor(url):
    scraper = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0', })
    response = scraper.get(url)
    htmlContent = response.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    return(soup, response)

def Page_Links(soup):
    anchors = soup.find_all('a')
    all_links = set()
    for link in anchors:
        if 'href' in link.attrs:
            page_url = link.get('href')
            if page_url.startswith('http') or (page_url.startswith('https') or page_url.startswith('www')):
                pass
            else:
                page_url = url + page_url

            all_links.add(page_url)
    return all_links

def Emails_Extractor(soup, response):

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com"
                                  , response.text, re.I))  # re.I: (ignore case)

    emails.update(new_emails)

url = 'http://www.burpple.com/sg'
soup, response = Soup_Extractor(url)
all_links = Page_Links(soup)
sleep(5)

for link in all_links:
    soup, response = Soup_Extractor(link)
#
    Emails_Extractor(soup, response)
print(emails)

