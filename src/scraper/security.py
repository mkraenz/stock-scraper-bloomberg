'''
Created on 15.05.2018

@author: Mirco
'''
import math


class Security(object):

    def __init__(self, symbol, scraper=None):
        self.symbol = symbol
        self.scraper = scraper
        self.name = ''
        self.price = math.inf
        self.book = 0
        self.shares_outstanding = 0
        self.earnings = 0
        self.sales = 0
        self.thirty_day_average_volume = 0
        self.latest_dividend = 0
    
    def price_to_book(self):
        return self.market_cap() / self.book
    
    def market_cap(self):
        return self.shares_outstanding * self.price
    
    def book_to_market(self):
        return self.book / self.market_cap()
    
    def price_to_earnings(self):
        return self.price / self.earnings
    
    def price_to_sales(self):
        return self.price / self.sales
    
    def earnings_per_share(self):
        return self.earnings / self.shares_outstanding
    
    def dividend_yield(self):
        return self.latest_dividend / self.price
    
    def update(self):
        self.scraper.set_url(self.symbol)
        self.scraper.update()
        self.name = self.scraper.scrape_name()
        self.price = self.scraper.scrape_price()
        self.shares_outstanding = self.scraper.scrape_shares_outstanding()
        self.book = self.scraper.scrape_book()
        self.earnings = self.scraper.scrape_earnings()
        self.sales = self.scraper.scrape_sales()
        self.thirty_day_average_volume = self.scraper.scrape_thirty_days_average_volume()
        self.latest_dividend = self.scraper.scrape_latest_dividend()
        
    def __str__(self):
        return str((self.name, self.symbol, self.price, self.shares_outstanding, self.book))
