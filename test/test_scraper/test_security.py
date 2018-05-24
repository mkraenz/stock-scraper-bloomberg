'''
Created on 15.05.2018

@author: Mirco
'''
import unittest
from unittest.mock import MagicMock
from scraper.security import Security


class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.stock = Security('EOAN')
        self.name = 'E.ON SE'
        self.stock.price = 10
        self.stock.book = 250
        self.stock.shares_outstanding = 50

    def test_price_to_book(self):
        self.assertEqual(self.stock.price_to_book(), 2)

    def test_market_cap(self):
        self.assertEqual(self.stock.market_cap(), 500)
        
    def test_book_to_market(self):
        self.assertEqual(self.stock.book_to_market(), 0.5)
        
    def test_to_string(self):
        self.assertTrue(str(self.stock))

        
class TestSecurityWithScraper(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        scraper_mock = MagicMock()
        scraper_mock.scrape_price.return_value = 10
        scraper_mock.scrape_book.return_value = 250
        scraper_mock.scrape_shares_outstanding.return_value = 50
        self.stock = Security('EOAN:GR', scraper_mock)
        
    def test_book(self):
        self.stock.update()
        self.assertEqual(250, self.stock.book)

        
if __name__ == "__main__":
    unittest.main()
