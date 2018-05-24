'''
Created on 21.05.2018

@author: Mirco
'''

class IExporter(object):

    def write(self, security_list):
        raise NotImplementedError("Class %s doesn't implement load_file()" % (self.__class__.__name__))