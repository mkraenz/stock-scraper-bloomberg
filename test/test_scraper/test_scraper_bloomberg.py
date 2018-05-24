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
        
        self.NAME = 'E.ON SE'
        self.PRICE = 9.29
        self.SHARES_OUTSTANDING = 2.2 * 10 ** 9
        self.PRICE_TO_BOOK = 4.5789
        self.BOOK = 4463517438.686148
        self.MARKET_CAP = self.PRICE * self.SHARES_OUTSTANDING
        self.PRICE_TO_EARNINGS = 4.81
        self.PRICE_TO_SALES = 0.5472
        self.THIRTY_DAYS_AVERAGE_VOLUME = 12684690
        self.LATEST_DIVIDEND = 0.3

    def load_html_test_data(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'bloomberg-eoan-2018-05-15.html')
        file = open(filename, 'r')
        html_example = file.read()
        file.close()
        return html_example
        
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.scraper = ScraperBloomberg('')
        self.scraper.update_html_soup(self.html_example)
        
    def test___parse_human_readable_number_to_int(self):
        self.assertEqual(1200000000, self.scraper._ScraperBloomberg__parse_human_readable_number_to_int('1.2B'))
        self.assertEqual(2300000, self.scraper._ScraperBloomberg__parse_human_readable_number_to_int('2.3M'))
        
    def test_scrape_name(self):
        self.assertEqual(self.scraper.scrape_name(), self.NAME)

    def test_scrape_price(self):
        self.assertEqual(self.scraper.scrape_price(), self.PRICE)
        
    def test_scrape_price_to_book(self):
        self.assertEqual(self.scraper.scrape_price_to_book(), self.PRICE_TO_BOOK)
        
    def test_scrape_shares_outstanding(self):
        self.assertEqual(self.scraper.scrape_shares_outstanding(), self.SHARES_OUTSTANDING)
        
    def test_scrape_book(self):
        self.assertEqual(self.scraper.scrape_book(), self.BOOK)
        
    def test_scrape_price_to_earnings(self):
        self.assertEqual(self.scraper.scrape_price_to_earnings(), self.PRICE_TO_EARNINGS)
        
    def test_scrape_price_to_sales(self):
        self.assertEqual(self.scraper.scrape_price_to_sales(), self.PRICE_TO_SALES)
        
    def test_scrape_thirty_days_average_volume(self):
        self.assertEqual(self.scraper.scrape_thirty_days_average_volume(), self.THIRTY_DAYS_AVERAGE_VOLUME)
        
    def test_scrape_latest_dividend(self):
        self.assertEqual(self.scraper.scrape_latest_dividend(), self.LATEST_DIVIDEND)
        
    def test_scrape_earnings(self): 
        self.assertEqual(self.scraper.scrape_earnings(), self.MARKET_CAP / self.PRICE_TO_EARNINGS)
        
    def test_scrape_sales(self):
        self.assertEqual(self.scraper.scrape_sales(), self.MARKET_CAP / self.PRICE_TO_SALES)
        
