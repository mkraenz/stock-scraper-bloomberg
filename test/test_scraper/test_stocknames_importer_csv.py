'''
Created on 21.05.2018

@author: Mirco
'''
import unittest
from scraper.stocknames_importer_csv import StocknamesImporterCSV


class TestStockNamesImporterCSV(unittest.TestCase):

    def test_iterator(self):
        names = ['Alphabet', 'Facebook Inc']
        symbols = ['GOOGL:US', 'FB:US']
        path_rel_to_stocknames_importer_csv = '../../test/test_scraper/test.csv'
        
        importer = StocknamesImporterCSV()
        importer.load_file(path_rel_to_stocknames_importer_csv)
        for pair in importer:
            self.assertIn(pair[0], names)
            self.assertIn(pair[1], symbols)
        importer.cleanup()


if __name__ == "__main__":
    unittest.main()
