'''
Created on 15.05.2018

@author: Mirco
'''
import unittest
from main.security import Security, SecurityDataMiner


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
        
class TestSecurityDataMiner(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.miner = SecurityDataMiner('')
        
    
    def test___parse_human_readable_number_to_int(self):
        self.assertEqual(1200000000, self.miner._SecurityDataMiner__parse_human_readable_number_to_int('1.2B'))
        self.assertEqual(2300000, self.miner._SecurityDataMiner__parse_human_readable_number_to_int('2.3M'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()