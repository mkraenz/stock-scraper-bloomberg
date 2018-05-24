'''
Created on 17.05.2018

@author: Mirco
'''
from scraper.builder import Builder
import sys
  

def main():
    if sys.argv[1] and sys.argv[2]:
        input_path_rel = sys.argv[1]
        output_path_rel = sys.argv[2]
    manager = Builder().create_manager(input_path_rel, output_path_rel)
    manager.manage()


if __name__ == '__main__':
    main()