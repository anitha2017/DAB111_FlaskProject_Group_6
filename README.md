# Final Project Group 6

## Requirements

We maintain the following structure, where each folder includes the specified information.

In the "data_collection" folder:

The Python file named "selenium_webdriver.py" and "fetchdealers.ipynb" serve the following purposes:
"selenium_webdriver.py" houses the method "fetch_dealerlist_webscraping," utilized for extracting information from a website through Selenium web drivers. Please note, that The location of "chromedriver.exe" is specified within this file.

"fetchdealers.ipynb" is a Jupyter notebook that executes the method defined in "selenium_webdriver.py." Additionally, this notebook handles data cleaning and writes the CSV file to the "data_processing" folder.

"chromedriver.exe" is also included in this folder, serving as the automation tool for web scraping via Chrome browser drivers.

In the "data_processing" folder:

The file "ford_dealers.xlsx" contains dealership data obtained through web scraping.
In the database folder:

The Python file "build_db.py" is responsible for creating "dealers.db" and inserting data into the "ford_dealers" table based on the information from "../data_processing/ford_dealers.xlsx."


## How to install the requirements.txt.

pip install -r requirements.txt

## we used below method to freeze the environment libraries to requirement.txt
pip list --format=freeze > requirements.txt



## known issue https://stackoverflow.com/questions/62885911/pip-freeze-creates-some-weird-path-instead-of-the-package-version