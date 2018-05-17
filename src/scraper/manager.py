'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.security import Security


class Manager(object):
    
    def __init__(self, importer, exporter, scraper, security_list):
        self.importer = importer
        self.exporter = exporter
        self.security_list = security_list
        self.scraper = scraper
    
    def manage(self):
        for pair in self.importer:
            sec = Security(pair[0], pair[1], self.scraper)
            self.security_list.append(sec)
        self.security_list.update()
        
        print(self.security_list)
