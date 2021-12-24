import os
from selenium import webdriver
import pandas as pd
import re
from bs4 import BeautifulSoup
import json
import time
import random
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
import json
import requests
from selenium.common.exceptions import TimeoutException

def get_property_info(driver):
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    holi = soup.find('script', id="__NEXT_DATA__", type="application/json").text
    holi = json.loads(holi)
    data = holi['props']['initialState']['realestate']['basic']
    
    return data

def load_page(url, driver):
    driver.get(url)
    time.sleep(10)

def main(url, keys, driver):
    load_page(url, driver)
    data = get_property_info(driver)
    new_data = [data.get(key) for key in keys]
    zip_iterator = zip(keys, new_data)
    a_dictionary = dict(zip_iterator) 

    return a_dictionary

def get_all_data(all_good_links, chromedriver_path):
    total_data = []
    bad_urls = {}
    
    options = Options()
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(chromedriver_path, options=options) #
    driver.set_page_load_timeout(60)
    time.sleep(10)

    keys = ['rentPrice', 'rentTotalPrice', 'area', 'areac', 'garages', 'sector', 'neighborhood',
            'commonNeighborhood', 'coordinates', 'detail', 'contactPhone', 'builtTime']

    for url in tqdm(all_good_links):
        try:
            try:
                a_dictionary = main(url, keys, driver)
                total_data.append(a_dictionary)
                
                with open("total_data.txt", "w") as fp:
                    json.dump(total_data, fp)
                
            except TimeoutException as ex:

                with open("total_data.txt", "w") as fp:
                    json.dump(total_data, fp)

                driver.quit()
                driver = webdriver.Chrome(chromedriver_path, options=options)
                driver.set_page_load_timeout(60)
                time.sleep(10)

                a_dictionary = main(url)
                total_data.append(a_dictionary)
        except Exception as e:
            bad_urls.update({url: str(e)})
            
            with open("bad_urls.txt", "w") as fp:
                json.dump(bad_urls, fp)    
    
    return total_data, bad_urls