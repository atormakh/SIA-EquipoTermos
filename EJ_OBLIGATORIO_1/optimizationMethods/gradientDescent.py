from autograd.misc.optimizers import sgd
from scipy.optimize import minimize
import numdifftools as nd
import numpy as np

class GradientDescent:

    METHOD_NAME = 'BFGS'

    
    def __init__(self):
        self.useGeneralAlgorithm = False

    def calculateOptimal(self,individual,function):
        # return sgd(nd.Gradient(function.error),np.array(individual.genes))
        return minimize(function.error,individual.genes,args=(0),method=self.METHOD_NAME).x 

    def calculateDirection(self,individual):
        return nd.Gradient(individual.genes)

    @classmethod
    def getMethod(cls):
        return cls()