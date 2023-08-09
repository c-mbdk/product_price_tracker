from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

import pandas as pd

tracker_columns = ["Shop", "Product", "In Stock", "Price"]

# Shop: Superdrug
def superdrug_price_check(url, product_name):

    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get(url)

    try:
        browser.find_element(By.CLASS_NAME, "out-of-stock")
        superdrug_data = pd.DataFrame([("Superdrug", product_name, "N","N/A")], columns=tracker_columns)
    except NoSuchElementException:
        product_price = browser.find_element(By.CLASS_NAME, "price__current")
        superdrug_data = pd.DataFrame([("Superdrug", product_name, "Y", product_price.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return superdrug_data
    

# Shop: Wilko
def wilko_price_check(url, product_name):
    
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get(url)

    try:
        browser.find_element(By.XPATH, "//h2[contains(., 'out of stock')]")
        wilko_data = pd.DataFrame([("Wilko", product_name, "N","N/A")], columns=tracker_columns)
    except NoSuchElementException:
        product_price_wilko = browser.find_element(By.CLASS_NAME, "pdp-price")
        wilko_data = pd.DataFrame([("Wilko", product_name, "Y", product_price_wilko.text)], columns=tracker_columns)
    finally:
        browser.quit()
        return wilko_data
    

# Shop: Boots
def boots_price_check(url, product_name):

    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
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
