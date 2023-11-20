from variables import product1_superdrug_url, product1_boots_url, product2_superdrug_url,\
    product2_boots_url, product3_boots_url, product3_superdrug_url

from scraper_functions import superdrug_price_check, boots_price_check

import pandas as pd

tracker_df = pd.DataFrame(columns=["Shop", "Product", "In Stock", "Price"])

# Product 1: Dettol Soap
product1_superdrug_check = superdrug_price_check(product1_superdrug_url)
product1_boots_check = boots_price_check(product1_boots_url)

# Product 2: Vaseline Body Oil
product2_superdrug_check = superdrug_price_check(product2_superdrug_url)
product2_boots_check = boots_price_check(product2_boots_url)

# Product 3: TheBreathCo Mouthwash - Icy Mint
product3_superdrug_check = superdrug_price_check(product3_superdrug_url)
product3_boots_check = boots_price_check(product3_boots_url)

# Compiling results
result_df_list = [
    product1_superdrug_check, 
                  product1_boots_check, 
                  product2_superdrug_check, 
                  product2_boots_check,
                  product3_superdrug_check, 
                  product3_boots_check]

for result in result_df_list:
    tracker_df = pd.concat([tracker_df, result], ignore_index=True)

tracker_df.to_csv("results.csv", index=False)
