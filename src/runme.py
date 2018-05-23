'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.builder import Builder
  
if __name__ == '__main__':
    manager = Builder().create()
    manager.manage()