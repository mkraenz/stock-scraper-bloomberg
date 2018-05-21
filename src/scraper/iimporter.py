'''
Created on 21.05.2018

@author: Mirco
'''

class IImporter(object):
    '''
    classdocs
    '''

    def load_file(self, relative_path):
        raise NotImplementedError("Class %s doesn't implement load_file()" % (self.__class__.__name__))
    
    def cleanup(self):
        raise NotImplementedError("Class %s doesn't implement cleanup()" % (self.__class__.__name__))

    def __iter__(self):
        raise NotImplementedError("Class %s doesn't implement __iter__()" % (self.__class__.__name__))