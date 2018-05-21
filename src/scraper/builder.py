'''
Created on 18.05.2018

@author: Mirco
'''
from scraper.scraper_bloomberg import ScraperBloomberg
from scraper.stocknames_importer_csv import StocknamesImporterCSV
from scraper.manager import Manager
from scraper.security_list import SecurityList
from scraper.exporter_csv import Exporter_CSV


class Builder(object):

    def start(self):
        importer = StocknamesImporterCSV()
        exporter = Exporter_CSV()
        scraper = ScraperBloomberg()
        manager = Manager(importer, exporter, scraper, SecurityList())
        
        manager.manage()
