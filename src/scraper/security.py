'''
Created on 15.05.2018

@author: Mirco
'''
import math
import urllib3
from bs4 import BeautifulSoup


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
    
    def set_book(self, price_to_book):
        self.book = 1 / price_to_book * self.market_cap()
        
    def update(self):
        self.scraper.update()
        self.price = self.scraper.scrape_price()
        self.shares_outstanding = self.scraper.scrape_shares_outstanding()
        self.set_book(self.scraper.scrape_price_to_book())
        
    def __str__(self):
        return str((self.name, self.symbol, self.price, self.shares_outstanding, self.book))
    
class ScraperBloomberg(object):
    
    html_soup = None    
    BASE_URL = 'https://www.bloomberg.com/quote/'
    
    def __init__(self, url=None):
        '''
        :param url: url to the website which shall be scraped
        '''
        if url: self.url = url
        self.html_soup = None
        
    def set_url(self, stock_symbol):
        self.url = self.BASE_URL + stock_symbol

    def update_html_soup(self, html_data):
        self.html_soup = BeautifulSoup(html_data, 'html.parser')

    def update(self):
        '''
        Download the website and prepare it for scraping.
        '''
        http = urllib3.PoolManager()
        request = http.request('GET', self.url, timeout=4.0)
        if request.status == 200:
            self.update_html_soup(request.data)

    def scrape_price(self):
        return float(self.__get_tag_text_by_class('priceText__1853e8a5').replace(",", ""))

    def __get_tag_text_by_class(self, html_class):
        tag = self.html_soup.find('span', attrs={'class':html_class})
        content = tag.text.strip()
        return content

    def __parse_human_readable_number_to_int(self, number_str):
        ''' Example: 1.2B = 1200000000, 2.3M = 2300000 '''
        number = float(number_str[:-1])
        if number_str[-1] == 'B':
            return int(number * (10 ** 9)) 
        elif number_str[-1] == 'M':
            return int(number * (10 ** 6)) 
        else:
            raise ValueError('Given number_str must end on "B" or "M".')
            
    def get_great_uncle_tag_by_text(self, text):
        shares_outstanding_string_tag = self.html_soup.find(text=text)
        great_uncle = shares_outstanding_string_tag.parent.parent.next_sibling
        return great_uncle

    def scrape_shares_outstanding(self):
        great_uncle = self.get_great_uncle_tag_by_text('Shares Outstanding')
        shares_outstanding = self.__parse_human_readable_number_to_int(great_uncle.text)
        return shares_outstanding
    
    def scrape_price_to_book(self):
        great_uncle = self.get_great_uncle_tag_by_text('Price to Book Ratio')
        return float(great_uncle.text)
        
if __name__ == '__main__':
    scraper = ScraperBloomberg()
    stock = Security('E.On SE', 'EOAN:GR', scraper)
    print(stock)
