'''
Created on 18.05.2018

@author: Mirco
'''
from scraper.importer_csv import ImporterCSV
from scraper.exporter_csv import Exporter_CSV
from scraper.scraper_bloomberg import ScraperBloomberg
from scraper.manager import Manager
from scraper.security_list import SecurityList


class Builder(object):

    def start(self):
        importer = ImporterCSV()
        exporter = Exporter_CSV()
        scraper = ScraperBloomberg()
        manager = Manager(importer, exporter, scraper, SecurityList())
        
        manager.manage()
