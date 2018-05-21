'''
Created on 17.05.2018

@author: Mirco
'''
import os
from scraper.iimporter import IImporter


class StocknamesImporterCSV(IImporter):
    
    def __init__(self):
        self.file = None

    def load_file(self, relative_path):
        ''' expects a file in the form "name,symbol\nname2,symbol2\n" where \n are line breaks (Return key)'''
        if self.file: self.cleanup()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, relative_path)
        self.file = open(filename, 'r')
# 
    def cleanup(self):
        self.file.close()

    def __next__(self):
        ''' @return tuple of stock name and stock symbol '''
        line = self.file.readline().replace('\n', '')
        if not line:
            raise StopIteration
        name, symbol = line.split(',')
        return name, symbol
    
    def __iter__(self):
        return self
