'''
Created on 17.05.2018

@author: Mirco
'''
import unittest
import os
from scraper.scraper_bloomberg import ScraperBloomberg

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
