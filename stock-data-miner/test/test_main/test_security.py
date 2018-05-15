'''
Created on 15.05.2018

@author: Mirco
'''
import unittest
from main.security import Security, SecurityDataMinerBloomberg


class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.stock = Security('E.On', 'EOAN')
        self.stock.price = 10
        self.stock.book = 250
        self.stock.shares_outstanding = 50


    def test_get_P_to_B(self):
        self.assertEqual(self.stock.get_P_to_B(), 0.04)

    def test_get_B_to_P(self):
        self.assertEqual(self.stock.get_B_to_P(), 25)
        
    def test_get_market_cap(self):
        self.assertEqual(self.stock.get_market_cap(), 500)
        
    def test_get_B_to_M(self):
        self.assertEqual(self.stock.get_B_to_M(), 0.5)
        
class TestSecurityDataMinerBloomberg(unittest.TestCase):
    
    file = open('bloomberg-eoan-2018-05-15.html', 'r')
    html_example = file.read()
    file.close()
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.miner = SecurityDataMinerBloomberg('')
        
    
    def test___parse_human_readable_number_to_int(self):
        self.assertEqual(1200000000, self.miner._SecurityDataMinerBloomberg__parse_human_readable_number_to_int('1.2B'))
        self.assertEqual(2300000, self.miner._SecurityDataMinerBloomberg__parse_human_readable_number_to_int('2.3M'))

    def test_mine_price(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_price(), 9.29)
        
    def test_mine_book_value(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_book_value(), 4.5789)
        
    def test_mine_shares_outstanding(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_shares_outstanding(), 2.2 * 10**9)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()