from scipy.optimize import minimize
import numdifftools as nd
import numpy as np

class GradientDescent:

    METHOD_NAME = 'BFGS'

    def calculateOptimal(self,individual,function):
        return minimize(function.error,individual.genes,args=(0),method=self.METHOD_NAME).x 

    @classmethod
    def getMethod(cls):
        return cls()