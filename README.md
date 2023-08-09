# product_price_tracker

## About this project
This project uses a series of functions to scrape websites for the price of certain products and produces a csv. There are other price comparison websites that work well, but this is more personalised to certain products that the author uses regularly.

The scraper now runs in headless mode i.e., it does not wait for the UI to be loaded, before scraping the websites. The time savings are currently minimal, but if the number of products/shops checked increases, the benefits will be more obvious.

## Future enhancements
There are some code adjustments that could be made. There is room to refactor the functions that scrape the websites and some variables could be renamed to be more generic. This will be improved in a future release.

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