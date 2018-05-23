'''
Created on 18.05.2018

@author: Mirco
'''
from scraper.importer_csv import ImporterCSV
from scraper.exporter_csv import Exporter_CSV
from scraper.manager import Manager
from scraper.security_list import SecurityList


class Builder(object):

    def create(self):
        importer = ImporterCSV()
        exporter = Exporter_CSV()
        return Manager(importer, exporter, SecurityList())
