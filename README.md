# Stock Scraper Bloomberg
[![Build Status](https://travis-ci.com/proSingularity/stock-scraper-bloomberg.svg?branch=master)](https://travis-ci.com/proSingularity/stock-scraper-bloomberg) [![codecov](https://codecov.io/gh/proSingularity/stock-scraper-bloomberg/branch/master/graph/badge.svg)](https://codecov.io/gh/proSingularity/stock-scraper-bloomberg)

## Installation
* Download repository from github.  
* Navigate into the project root. 
* From command line run
`pip install ./src`

## Supported Python versions
* 3.5
* 3.6

For details on other versions see [Travis build Issue #29](https://travis-ci.com/proSingularity/stock-scraper-bloomberg)

## Script Usage example
After installation navigate to project root.  
From  command line run  
```$ python src/scraper/scraper_cli.py run [relative_input_path.txt] [relative_output_path.csv]```

Your *input_file.txt* should look like this:
```
GOOGL:US
FB:US
...
```
That is, the ticker symbol of each company as found on bloomberg.com. One symbol per line.

Example *outputfile.csv* from 2018/05/24
```
name,symbol,price,book,shares outstanding,price to book,market cap,book to market
Alphabet Inc,GOOGL:US,1085.96,69115802241.82756,298660000,4.6926,324332813600.0,0.21310147892426373
Facebook Inc,FB:US,186.9,64192795912.81824,2400000000,6.9877,448560000000.0,0.1431086051204259
```

## API Usage example
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
* fire for command line interface

## Previous name
stock-data-miner
