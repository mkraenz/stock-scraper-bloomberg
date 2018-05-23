'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.security import Security
from scraper.i_exporter import IExporter
from scraper.i_importer import IImporter
from scraper.scraper_bloomberg import ScraperBloomberg


class Manager(object):
    
    def __init__(self, importer, exporter, security_list):
        '''
        :param importer: instance of IImporter
        :param exporter: instance of IExporter
        :param security_list:
        '''
        assert isinstance(importer, IImporter)
        assert isinstance(exporter, IExporter)
        self.importer = importer
        self.exporter = exporter
        self.security_list = security_list

    def fill_security_list(self, importer):
        for pair in importer:
            sec = Security(pair[0], pair[1], ScraperBloomberg())
            self.security_list.append(sec)

    def manage(self):
        file_path_relative_to_importer = '../../test/test_scraper/test.csv'
        self.importer.load_file(file_path_relative_to_importer)
        self.fill_security_list(self.importer)
        self.security_list.update()
        
        self.importer.cleanup()
        self.exporter.write('testOutput', self.security_list)
