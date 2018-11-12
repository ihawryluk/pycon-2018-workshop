# -*- coding: utf-8 -*-

    
class Calc:
    def add(self, *args):
        return sum(args)
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        if a == 0 or b == 0:
            raise ValueError
        return a * b
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'
# the below works and is correct TDD-wise, it is not pretty though       
#        if b == 0:
#            return 'inf'
#        return a / b
            
    def avg(self, container, downLimit = None, upLimit = None):
        if downLimit != None:
            container = [el for el in container if el > downLimit]
        if upLimit != None:
            container = [el for el in container if el < upLimit]
        if not len(container): # meaning that container is empty
            return 'inf'
        return sum(container) / len(container)
    
    def untested_function():
        return 'This is just to check the coverage'
        
    