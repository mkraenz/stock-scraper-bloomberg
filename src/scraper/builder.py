'''
Created on 18.05.2018

@author: Mirco
'''
from scraper.scraper_bloomberg import ScraperBloomberg
from scraper.stocknames_importer_csv import StocknamesImporterCSV
from scraper.manager import Manager
from scraper.security_list import SecurityList


class Builder(object):

    def start(self):
        importer = StocknamesImporterCSV()
        importer.load_file('../../test/test_scraper/test.csv')
        scraper = ScraperBloomberg()
        manager = Manager(importer, None, scraper, SecurityList())
        
        manager.manage()
