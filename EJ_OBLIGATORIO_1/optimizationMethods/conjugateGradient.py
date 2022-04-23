from scipy.optimize import minimize

class ConjugateGradient:

    METHOD_NAME = 'CG'

    def __init__(self):
        self.useGeneralAlgorithm = False

    def calculateOptimal(self,individual,function):
        return minimize(function.error,individual.genes,args=(0),method=self.METHOD_NAME).x 

    def calculateDirection(self,individual):
        return None

    @classmethod
    def getMethod(cls):
        return cls()