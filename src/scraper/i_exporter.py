'''
Created on 21.05.2018

@author: Mirco
'''

class IExporter(object):

    def write(self, security_list):
        raise NotImplementedError("Class %s doesn't implement load_file()" % (self.__class__.__name__))
    
    def get_header(self):
        return [
            'name',
            'symbol',
            'price',
            'book',
            'shares outstanding',
            'price to book',
            'market cap',
            'book to market',
        ]
        
    def get_security_data(self, security):
        return [
            security.name,
            security.symbol,
            security.price,
            security.book,
            security.shares_outstanding,
            security.price_to_book(),
            security.market_cap(),
            security.book_to_market()
            ]
