'''
Created on 24.05.2018

@author: Mirco
'''
from fire.core import Fire
from scraper.builder import Builder

class ScraperCLI(object):

    def run(self,input_path_rel, output_path_rel):
        ''' 
        example: 
        from project root stock-scraper-bloomberg run
        $ python src/scraper/scraper_cli.py run test/test.csv test/output.csv
        '''
        manager = Builder().create_manager(input_path_rel, output_path_rel)
        manager.manage()
    
    
if __name__ == '__main__':
    Fire(ScraperCLI())