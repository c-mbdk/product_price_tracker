# product_price_tracker

## About this project
This project uses a series of functions to scrape websites for the price of certain products and produces a csv. There are other price comparison websites that work well, but this is more personalised to certain products that the author uses regularly.

The scraper can run in headless mode i.e., it does not have to wait for the UI to be loaded, before scraping the websites. The time savings are currently minimal, but if the number of products/shops checked increases, the benefits will be more obvious. However, the scraper fails at the first hurdle when headless mode is enabled: accepting the cookies on the current page. For now, headless mode has not been enabled.

GitHub Actions has been used to schedule the regular execution of the scraper, with the results sent by email. For testing, the workflow was triggered by pushing commits to the main branch, including merge commits from a feature branch.

## Future enhancements
There are some code adjustments that could be made, like refactoring the functions that scrape the websites. 

The workflow is not consistently triggered at the scheduled time. As this is a personal project, this is not a major concern. But third-party scheduling services like Zapier and Cronhub could be used to request the GitHub API to trigger the workflow.

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
$ (env) python3 scraper.py
```