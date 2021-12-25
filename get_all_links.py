from selenium import webdriver
import re
import json
import time
import random
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options

def get_dirty_links(driver):
    elems = driver.find_elements_by_xpath("//a[@href]")
    all_links = [elem.get_attribute("href") for elem in elems]
    all_links = list(set(all_links))
    
    return all_links

def get_good_links(all_links):
    pattern = r'https://www.metrocuadrado.com/inmueble\S+'
    good_links = [x for x in all_links if bool(re.match(pattern, x))]
    
    return list(set(good_links))

def next_page(driver):
    busquedas_sugeridas = "/html/body/div[2]/div/div/div[2]/div[2]/section/div[1]/div/div/h2" #"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul[2]/li[12]"
    next_page = driver.find_element_by_xpath(busquedas_sugeridas)
    
    next_page.location_once_scrolled_into_view
    
    next_page_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul[2]/li[12]"
    next_page = driver.find_element_by_xpath(next_page_xpath)
    
    next_page.click()

def get_all_links(chromedriver_path, ciudad, tipo_inmueble):
    options = Options()
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(chromedriver_path, options=options)
    time.sleep(10)
    driver.get('https://www.metrocuadrado.com/'+tipo_inmueble+'/arriendo/'+ciudad)
    time.sleep(10)
    
    all_good_links = []

    for i in tqdm(range(0, 205)):
        try:
            all_links = get_dirty_links(driver)
            good_links = get_good_links(all_links)
            
            all_good_links.append(good_links)
            next_page(driver)
            
            time_2_sleep = random.randint(10, 30)
            time.sleep(time_2_sleep)
        except Exception as e:
            print(e)
            pass
    
    flat_list = [item for sublist in all_good_links for item in sublist]
    all_good_links = list(set(flat_list))
    
    with open("all_good_links.txt", "r") as fp:
        all_good_links = json.load(fp)
    
    return all_good_links