'''
Created on 17.05.2018

@author: Mirco
'''
import os
from scraper.i_importer import IImporter


class Importer(IImporter):
    
    def __init__(self, input_path_rel):
        self.input_path_rel = input_path_rel
        self.file = None

    def load_file(self):
        ''' expects a file in the form "name,symbol\nname2,symbol2\n" where \n are line breaks (Return key)'''
        if self.file: self.cleanup()
        cwd = os.getcwd()
        filename = os.path.join(cwd, self.input_path_rel)
        self.file = open(filename, 'r')

# 
    def cleanup(self):
        self.file.close()

    def __next__(self):
        ''' @return tuple of stock name and stock symbol '''
        line = self.file.readline().replace('\n', '')
        if not line:
            raise StopIteration
        return line
    
    def __iter__(self):
        return self
