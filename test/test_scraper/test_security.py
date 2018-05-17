'''
Created on 15.05.2018

@author: Mirco
'''
import os

import unittest
from unittest.mock import MagicMock
from scraper.security import Security
from scraper.scraper_bloomberg import ScraperBloomberg

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.stock = Security('E.On', 'EOAN')
        self.stock.price = 10
        self.stock.book = 250
        self.stock.shares_outstanding = 50

    def test_price_to_book(self):
        self.assertEqual(self.stock.price_to_book(), 2)

    def test_market_cap(self):
        self.assertEqual(self.stock.market_cap(), 500)
        
    def test_book_to_market(self):
        self.assertEqual(self.stock.book_to_market(), 0.5)
        
class TestSecurityWithScraper(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        scraper_mock = MagicMock()
        scraper_mock.scrape_price.return_value = 10
        scraper_mock.scrape_book.return_value = 250
        scraper_mock.scrape_shares_outstanding.return_value = 50
        self.stock = Security('E.On SE', 'EOAN:GR', scraper_mock)
        
    def test_book(self):
        self.assertEqual(250, self.stock.book)
        
class TestScraperBloomberg(unittest.TestCase):

    def __init__(self, tests=()):
        super().__init__(tests)
        self.html_example = self.load_html_test_data()

    def load_html_test_data(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'bloomberg-eoan-2018-05-15.html')
        file = open(filename, 'r')
        html_example = file.read()
        file.close()
        return html_example
        
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.miner = ScraperBloomberg('')
    
    def test___parse_human_readable_number_to_int(self):
        self.assertEqual(1200000000, self.miner._ScraperBloomberg__parse_human_readable_number_to_int('1.2B'))
        self.assertEqual(2300000, self.miner._ScraperBloomberg__parse_human_readable_number_to_int('2.3M'))

    def test_mine_price(self):
        self.miner.update_html_soup(self.html_example)
        self.assertEqual(self.miner.scrape_price(), 9.29)
        
    def test_mine_price_to_book(self):
        self.miner.update_html_soup(self.html_example)
        self.assertEqual(self.miner.scrape_price_to_book(), 4.5789)
        
    def test_mine_shares_outstanding(self):
        self.miner.update_html_soup(self.html_example)
        self.assertEqual(self.miner.scrape_shares_outstanding(), 2.2 * 10 ** 9)

if __name__ == "__main__":
    unittest.main()
