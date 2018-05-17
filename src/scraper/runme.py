'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.scraper_bloomberg import ScraperBloomberg
from scraper.security import Security
  
if __name__ == '__main__':
    scraper = ScraperBloomberg()
    stock = Security('E.On SE', 'EOAN:GR', scraper)
    print(stock)