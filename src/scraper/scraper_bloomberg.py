'''
Created on 17.05.2018

@author: Mirco
'''
from bs4 import BeautifulSoup
import urllib3
from scraper.iscraper import IScraper


class ScraperBloomberg(IScraper):
    
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
    
    def scrape_book(self):
        price_to_book = self.scrape_price_to_book()
        shares_outstanding = self.scrape_shares_outstanding()
        price = self.scrape_price()
        market_cap = shares_outstanding * price
        return 1 / price_to_book * market_cap
        
