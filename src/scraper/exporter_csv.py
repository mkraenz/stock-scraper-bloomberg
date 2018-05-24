'''
Created on 21.05.2018

@author: Mirco
'''
from scraper.i_exporter import IExporter
import csv
import os


class Exporter_CSV(IExporter):
    
    def __init__(self, output_path_rel):
        self.output_path_rel = output_path_rel
            
    def write(self, security_list):
        filename = os.path.join(os.getcwd(), self.output_path_rel)
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.get_header())
            for security in security_list:
                writer.writerow(self.get_security_data(security))
