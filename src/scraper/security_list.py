'''
Created on 18.05.2018

@author: Mirco
'''


class SecurityList(list):
    
    def update(self):
        for security in self:
            security.update()
            
    def __str__(self):
        return str([str(security) for security in self])
    
