from variables import dettol_superdrug_url, dettol_boots_url, dettol_wilko_url, vaseline_superdrug_url,\
    vaseline_boots_url, mouthwash_boots_url, mouthwash_superdrug_url

from variables import soap_name, oil_name, mouthwash_name

from scraper_functions import superdrug_price_check, wilko_price_check, boots_price_check

import pandas as pd

# from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager

# TODO: make headless
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

tracker_df = pd.DataFrame(columns=["Shop", "Product", "In Stock", "Price"])

# Product: Dettol Soap
soap_superdrug_check = superdrug_price_check(dettol_superdrug_url, soap_name)
soap_wilko_check = wilko_price_check(dettol_wilko_url, soap_name)
soap_boots_check = boots_price_check(dettol_boots_url, soap_name)

# Product: Vaseline Body Oil
body_oil_superdrug_check = superdrug_price_check(vaseline_superdrug_url, oil_name)
body_oil_boots_check = boots_price_check(vaseline_boots_url, oil_name)

# Product: TheBreathCo Mouthwash - Icy Mint
mouthwash_superdrug_check = superdrug_price_check(mouthwash_superdrug_url, mouthwash_name)
mouthwash_boots_check = boots_price_check(mouthwash_boots_url, mouthwash_name)

# Compiling results
result_df_list = [soap_superdrug_check, soap_wilko_check, soap_boots_check, body_oil_superdrug_check, body_oil_boots_check,
                  mouthwash_superdrug_check, mouthwash_boots_check]

for result in result_df_list:
    tracker_df = pd.concat([tracker_df, result], ignore_index=True)

tracker_df.to_csv("results.csv", index=False)
