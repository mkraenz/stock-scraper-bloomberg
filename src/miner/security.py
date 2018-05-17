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

    def __init__(self, name, symbol):
        '''
        Constructor
        '''
        self.name = name
        self.symbol = symbol
        self.price = math.inf
        self.book = 0
        self.shares_outstanding = 0
    
    def get_P_to_B(self):
        return self.price / self.book
    
    def get_B_to_P(self):
        return self.book / self.price
    
    def get_market_cap(self):
        return self.shares_outstanding * self.price
    
    def get_B_to_M(self):
        return self.book / self.get_market_cap()
    
    def set_book(self, price_to_book):
        self.book = self.price / price_to_book
    
    
class SecurityDataMinerBloomberg(object):
    
    html_soup = None
    
    def __init__(self, url):
        '''
        :param url: url to the website which shall be scraped
        '''
        self.url = url
        self.html_soup = None
        

    def update_html_soup(self, html_data):
        self.html_soup = BeautifulSoup(html_data, 'html.parser')

    def update_html(self):
        '''
        Download the website and prepare it for scraping.
        '''
        http = urllib3.PoolManager()
        request = http.request('GET', self.url, timeout=4.0)
        if request.status == 200:
            self.update_html_soup(request.data)

    def mine_price(self):
        return float(self.__get_tag_text_by_class('priceText__1853e8a5').replace(",", ""))
    

    def __get_tag_text_by_class(self, html_class):
        tag = self.html_soup.find('span', attrs={'class':html_class})
        content = tag.text.strip()
        return content


    def __parse_human_readable_number_to_int(self, number_str):
        ''' Example: 1.2B = 1200000000, 2.3M = 2300000
        '''
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

    def mine_shares_outstanding(self):
        text = 'Shares Outstanding'
        great_uncle = self.get_great_uncle_tag_by_text(text)
        shares_outstanding = self.__parse_human_readable_number_to_int(great_uncle.text)
        return shares_outstanding
    
    def mine_price_to_book(self):
        text = 'Price to Book Ratio'
        great_uncle = self.get_great_uncle_tag_by_text(text)
        return float(great_uncle.text)
        
    
    
if __name__ == '__main__':
    URL = 'https://www.bloomberg.com/quote/GOOGL:US'
    miner = SecurityDataMinerBloomberg(URL)
    miner.update_html()
    print('price = ', miner.mine_price())
    print('shares outstanding = ', miner.mine_shares_outstanding())
    print('price-to-book =', miner.mine_price_to_book())
    
