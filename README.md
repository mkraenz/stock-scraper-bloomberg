# Stock Scraper Bloomberg
[![Build Status](https://travis-ci.com/proSingularity/stock-scraper-bloomberg.svg?branch=master)](https://travis-ci.com/proSingularity/stock-scraper-bloomberg) [![codecov](https://codecov.io/gh/proSingularity/stock-scraper-bloomberg/branch/master/graph/badge.svg)](https://codecov.io/gh/proSingularity/stock-scraper-bloomberg)

## Installation
`pip install [path_to_project]/src/.`

## Usage example
Example from interactive python console `python -i`
```
>>> from scraper.security import Security
>>> from scraper.scraper_bloomberg import ScraperBloomberg
>>> scraper = ScraperBloomberg()
>>> security = Security('Alphabet', 'GOOGL:US', scraper)
>>> security.update()
>>> security.market_cap()
319458682400.0
```

## Currently available data from class Security
via `security.[command_from_list]`
* name
* symbol
* price
* book
* shares_oustanding
* price_to_book()
* market_cap()
* book_to_market()

## Technologies and tools

* Python 3
* setuptools for packaging
* Travis CI for continuous integration 
* codecov.io for code coverage
* BeautifulSoup4 for web scraping
* unittest for unit testing

## Previous name
stock-data-miner
