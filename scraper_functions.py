from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

from chromedriver_py import binary_path

import os

import pandas as pd



tracker_columns = ["Shop", "Product", "In Stock", "Price"]

def create_driver_instance():
    options = Options()
    # options.add_argument('--headless=new') - can't accept cookies when this is enabled
    options.add_argument('--no-sandbox')
    options.binary_location = "/opt/hostedtoolcache/chromium/latest/x64/chrome"
    service = Service(executable_path=binary_path)

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(3)
    return driver_instance


# Shop: Superdrug
def superdrug_price_check(url):
    browser = create_driver_instance()
    browser.get(url)

    cookies_button = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    cookies_button.click()

    try:
        browser.find_element(By.XPATH, "//span[contains(text(), 'Notify when in stock')]")
    except NoSuchElementException:
        product_price = browser.find_element(By.XPATH, "//span[@class='price__current']")
        product_title = browser.find_element(By.XPATH, "//h1[@class='product-details-title__text']")
        superdrug_data = pd.DataFrame([("Superdrug", product_title.text, "Y", product_price.text)], columns=tracker_columns)
    else:
        product_title = browser.find_element(By.XPATH, "//h1[@class='product-details-title__text']")
        superdrug_data = pd.DataFrame([("Superdrug", product_title.text, "N","N/A")], columns=tracker_columns)
    finally:
        browser.quit()
        return superdrug_data
    

# Shop: Boots
def boots_price_check(url):

    browser = create_driver_instance()
    browser.get(url)

    cookies_button = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    cookies_button.click()

    try:
        browser.find_element(By.ID, "add2CartBtn") # only present when the item is in stock
    except NoSuchElementException:
        product_title = browser.find_element(By.ID, "estore_product_title")
        boots_data = pd.DataFrame([("Boots", product_title.text, "N","N/A")], columns=tracker_columns)
    else:
        product_price_boots = browser.find_element(By.ID, "PDP_productPrice")
        product_title = browser.find_element(By.ID, "estore_product_title")
        boots_data = pd.DataFrame([("Boots", product_title.text, "Y", product_price_boots.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return boots_data
