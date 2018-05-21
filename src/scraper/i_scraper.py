'''
Created on 17.05.2018

@author: Mirco
'''

        
class IScraper(object):
    
    def set_url(self, stock_symbol):
        raise NotImplementedError("Class %s doesn't implement set_url()" % (self.__class__.__name__))

    def update(self):
        raise NotImplementedError("Class %s doesn't implement update()" % (self.__class__.__name__))
    
    def scrape_price(self):
        raise NotImplementedError("Class %s doesn't implement scrape_price()" % (self.__class__.__name__))
    
    def scrape_shares_outstanding(self):
        raise NotImplementedError("Class %s doesn't implement scrape_shares_outstanding()" % (self.__class__.__name__))
        
    def scrape_book(self):
        raise NotImplementedError("Class %s doesn't implement scrape_book()" % (self.__class__.__name__))
