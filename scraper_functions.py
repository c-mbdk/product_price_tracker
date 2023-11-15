from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

import pandas as pd

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

tracker_columns = ["Shop", "Product", "In Stock", "Price"]

def create_driver_instance():
    options = Options()
    options.add_argument('--headless=new')

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(1)
    return driver_instance


# Shop: Superdrug
def superdrug_price_check(url, product_name):
    browser = create_driver_instance()
    browser.get(url)

    try:
        browser.find_element(By.XPATH, "//span[contains(text(), 'Notify when in stock')]")
        superdrug_data = pd.DataFrame([("Superdrug", product_name, "N","N/A")], columns=tracker_columns)
    except NoSuchElementException:
        product_price = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='price__current']")))
        superdrug_data = pd.DataFrame([("Superdrug", product_name, "Y", product_price.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return superdrug_data
    

# Shop: Wilko
def wilko_price_check(url, product_name):
    
    browser = create_driver_instance()
    browser.get(url)

    try:
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//h2[contains(text(), 'out of stock')]")))
        wilko_data = pd.DataFrame([("Wilko", product_name, "N","N/A")], columns=tracker_columns)
    except NoSuchElementException:
        product_price_wilko = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'pdp-price')]")))
        wilko_data = pd.DataFrame([("Wilko", product_name, "Y", product_price_wilko.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return wilko_data
    

# Shop: Boots
def boots_price_check(url, product_name):

    browser = create_driver_instance()
    browser.get(url)

    try:
        browser.find_element(By.ID, "add2CartBtn") # only present when the item is in stock
    except NoSuchElementException:
        boots_data = pd.DataFrame([("Boots", product_name, "N","N/A")], columns=tracker_columns)
    else:
        product_price_boots = browser.find_element(By.ID, "PDP_productPrice")
        boots_data = pd.DataFrame([("Boots", product_name, "Y", product_price_boots.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return boots_data
