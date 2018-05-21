'''
Created on 21.05.2018

@author: Mirco
'''
from scraper.i_exporter import IExporter
import csv


class Exporter_CSV(IExporter):

            
    def write(self, file_name, security_list):
        ''' @parameter file_name: only the name, method attaches .csv '''
        with open(file_name + '.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.get_header())
            for security in security_list:
                writer.writerow(self.get_security_data(security))

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
