'''
Created on 15.05.2018

@author: Mirco
'''
import math

class Security(object):
    '''
    classdocs
    '''


    def __init__(self, name, symbol):
        '''
        Constructor
        '''
        self.name = name
        self.symbol = symbol
        self.price = math.inf
        self.book = 0
        self.shares_outstanding = 0
    
    def get_P_to_B(self):
        return self.price / self.book
    
    def get_B_to_P(self):
        return self.book / self.price
    
    def get_market_cap(self):
        return self.shares_outstanding*self.price
    
    def get_B_to_M(self):
        return self.book / self.get_market_cap()