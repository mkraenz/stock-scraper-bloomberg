'''
Created on 18.05.2018

@author: Mirco
'''
from scraper.importer_csv import ImporterCSV
from scraper.exporter_csv import Exporter_CSV
from scraper.manager import Manager
from scraper.security_list import SecurityList


class Builder(object):

    def create_manager(self, input_path_rel, output_path_rel):
        importer = ImporterCSV(input_path_rel)
        exporter = Exporter_CSV(output_path_rel)
        return Manager(importer, exporter, SecurityList())
