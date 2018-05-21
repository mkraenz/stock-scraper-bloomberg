'''
Created on 21.05.2018

@author: Mirco
'''

class IExporter(object):

    def write(self, file_name, security_list):
        ''' @parameter file_name: only the name, without e.g. .csv '''
        raise NotImplementedError("Class %s doesn't implement load_file()" % (self.__class__.__name__))