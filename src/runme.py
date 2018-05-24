'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.builder import Builder
  

def main():
    manager = Builder().create_manager('../test/test_scraper/test_input.txt', '../test/output.csv')
    manager.manage()


if __name__ == '__main__':
    main()