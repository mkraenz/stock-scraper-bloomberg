'''
Created on 21.05.2018

@author: Mirco
'''
import unittest
from scraper.importer_csv import ImporterCSV


class TestStockNamesImporterCSV(unittest.TestCase):

    def test_iterator(self):
        symbols = ['GOOGL:US', 'FB:US']
#         path_rel_to_project_root = 'test_scraper/test.csv' # for eclipse
        path_rel_to_project_root = 'test/test_scraper/test.csv' # for travis and official setup
        
        importer = ImporterCSV(path_rel_to_project_root)
        importer.load_file()
        for symbol in importer:
            self.assertIn(symbol, symbols)
        importer.cleanup()


if __name__ == "__main__":
    unittest.main()
