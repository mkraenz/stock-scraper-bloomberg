'''
Created on 21.05.2018

@author: Mirco
'''
import unittest
from scraper.importer_csv import ImporterCSV


class TestStockNamesImporterCSV(unittest.TestCase):

    def test_iterator(self):
        names = ['Alphabet', 'Facebook Inc']
        symbols = ['GOOGL:US', 'FB:US']
        path_rel_to_project_root = 'test/test_scraper/test.csv'
        
        importer = ImporterCSV(path_rel_to_project_root)
        importer.load_file()
        for pair in importer:
            self.assertIn(pair[0], names)
            self.assertIn(pair[1], symbols)
        importer.cleanup()


if __name__ == "__main__":
    unittest.main()
