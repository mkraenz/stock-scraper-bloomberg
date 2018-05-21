'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.security import Security
from scraper.iimporter import IImporter
from scraper.iscraper import IScraper


class Manager(object):
    
    def __init__(self, importer, exporter, scraper, security_list):
        assert isinstance(importer, IImporter)
#         assert isinstance(exporter, IExporter)
        assert isinstance(scraper, IScraper)
        self.importer = importer 
        self.exporter = exporter
        self.security_list = security_list
        self.scraper = scraper
    
    def manage(self):
        file_path_relative_to_importer = '../../test/test_scraper/test.csv'
        self.importer.load_file(file_path_relative_to_importer)
        for pair in self.importer:
            sec = Security(pair[0], pair[1], self.scraper)
            self.security_list.append(sec)
        self.security_list.update()
        
        print(self.security_list)
        self.importer.cleanup()