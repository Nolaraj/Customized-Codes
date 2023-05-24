url = "chrome-extension://lgmpcpglpngdoalbgeoldeajfclnhafa/popup.html"



delay = 5
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)
# driver.get(url)





from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import cloudscraper
from bs4 import BeautifulSoup
from itertools import permutations
import os

import time
Password = "12345678M"
dataset = [
# "above",                 #5
"harsh",
"obvious",
# "kind",                 #9
# "rabbit",                 #1
# "obey",                 #2
# "edge",                 #12
"sadness",
# "hammer",               #4
"nation",
"ramp"]
# "panda"]                #7

permutations_list = list(permutations(dataset))





options = Options()
options.add_extension('wallet.crx')

driver = webdriver.Chrome(options=options)


def image_checkpoint_return_location(image, confidence = 0.5):
    try:
        location = pyautogui.locateOnScreen(image, confidence=confidence) #For Confidence to be used in Code pip install opencv-python is needed
        if location is not None:
            return (location)
        else:
            print(f'{image} position is None during runtime')
            #Active value not set as per required by code error
            if image == "longitudinal_reinforcing.png":
                print(f'Set {image} as active before running the code')
            return (location)
    except:
        print(f'{image} is not available in the screen during runtime')

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


def get_data(driver):
    # Popup page
    driver.get(url)
    time.sleep(2)
    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen("url_entry.png", 0.95)))
    pyautogui.hotkey('enter')

    #clicking on the button of page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//button[@class="ant-btn ant-btn-primary ant-btn-lg"]'))).click()


    #Clicking on the Flex type of object
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".itemHover.cur.contentBox.lg.sfpItemBox.flex-space-between.mt16.allBorder"))).click()


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(Password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'confirmPassword'))).send_keys(Password)


    driver.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()








    # i = 0
    # while i != len(permutations_list):
    #     print(i)
    #     if




    time.sleep(2)
    for index1, perm in enumerate(permutations_list):
            list1 = []
            for item in perm:
                list1.append(item)
            list1.insert(0, "rabbit")
            list1.insert(1, "obey")
            list1.insert(3, "hammer")
            list1.insert(4, "above")
            list1.insert(6, "panda")
            list1.insert(8, "kind")
            list1.insert(11, "edge")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="#/ImportMnemonicsTip"]'))).click()

            WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]'))).click()

            for index, items in enumerate(list1):
                ID_name = f'mnemonics{index}'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ID_name))).send_keys(items)

            WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]'))).click()

            time.sleep(0.5)


            # check if the element is present
            if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'error.mt10'))) is not None:
                if index1 == 4:

#----------------------------------------------------------------------------------------------

                    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                        (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]'))).click()
                    # time.sleep(500)
                    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                        (By.XPATH,'a[href="#icon-more"]'))).click()


                    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                        (By.XPATH, '//use[@xlink:href="#icon-more"]'))).click()
                    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                        (By.XPATH, '//use[@xlink:href="#icon-add"]'))).click()



                    # driver.find_element(By.XPATH, '//use[@xlink:href="#icon-more"]').click()
                    #
                    # driver.find_element(By.XPATH, '//use[@xlink:href="#icon-add"]').click()

                    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                        (By.CLASS_NAME, "ant-dropdown-menu-title-content"))).click()


                    # Click on the element

#----------------------------------------------------------------------------------------------


                    #
                    #
                    #
                    # balance_element = driver.find_element(By.CSS_SELECTOR, "div.balance.h1")
                    # balance_text = balance_element.text
                    # print(balance_text)
                    #
                    # time.sleep(500)










                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "backIcon")))
                element.click()





            else:
                time.sleep(500)
                print("Element not found.")









os.chdir(os.path.join(os.getcwd(),"External Files", "Safe Pal"))
get_data(driver)


# soup, response = Soup_Extractor(url)
# all_links = Page_Links(soup)
#
#
#





