# product_price_tracker

## About this project
This project uses a series of functions to scrape websites for the price of certain products and produces a csv. There are other price comparison websites that work well, but this is more personalised to certain products that the author uses regularly.

## Future enhancements
There are some code adjustments that could be made. There is room to refactor the functions that scrape the websites and some variables could be renamed to be more generic. This will be improved in a future release.

Beyond repetitive code, it is possible to explore headless webscraping with this. Headless webscraping is known to be faster as it does not rely on loading the UI. Currently, when the scraper code is executed, it opens each browser window. As only a few links are currently used, the time taken for scraper code to be executed is still relatively short. However, the time savings with headless webscraping could be greater if the number of products/websites checked increases.

The scraper could also be scheduled to run regularly and the results sent by email. This can be worked on in a future release.

## How to Run

1. Install virtualenv:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:

Windows
```
$ .\env\Scripts\activate
```

MacOS/Unix
```
$ source env/bin/activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Run the scraper.py script:
```
$ python3 scraper.py
```