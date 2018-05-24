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
            'earnings',
            'price to earnings',
            'EPS',
            'sales',
            'price to sales',
            '30 days average volume',
            'latest dividend',
            'dividend yield',
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
            security.book_to_market(),
            security.earnings,
            security.price_to_earnings(),
            security.earnings_per_share(),
            security.sales,
            security.price_to_sales(),
            security.thirty_day_average_volume,
            security.latest_dividend,
            security.dividend_yield(),
            ]
