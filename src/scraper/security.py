'''
Created on 15.05.2018

@author: Mirco
'''
import math
from scraper.scraper_bloomberg import ScraperBloomberg


class Security(object):
    '''
    classdocs
    '''

    def __init__(self, name, symbol, scraper=None):
        self.name = name
        self.symbol = symbol
        if scraper:
            self.scraper = scraper
            scraper.set_url(self.symbol)
            self.update()
        else:
            self.price = math.inf
            self.book = 0
            self.shares_outstanding = 0
    
    def price_to_book(self):
        return self.market_cap() / self.book
    
    def market_cap(self):
        return self.shares_outstanding * self.price
    
    def book_to_market(self):
        return self.book / self.market_cap()
    
    def update(self):
        self.scraper.update()
        self.price = self.scraper.scrape_price()
        self.shares_outstanding = self.scraper.scrape_shares_outstanding()
        self.book = self.scraper.scrape_book()
        
    def __str__(self):
        return str((self.name, self.symbol, self.price, self.shares_outstanding, self.book))
    
    
if __name__ == '__main__':
    scraper = ScraperBloomberg()
    stock = Security('E.On SE', 'EOAN:GR', scraper)
    print(stock)
