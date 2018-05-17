'''
Created on 17.05.2018

@author: Mirco
'''

        
class IScraper(object):
    
    def set_url(self, stock_symbol):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
    
    def scrape_price(self):
        raise NotImplementedError
    
    def scrape_shares_outstanding(self):
        raise NotImplementedError
        
    def scrape_book(self):
        raise NotImplementedError
