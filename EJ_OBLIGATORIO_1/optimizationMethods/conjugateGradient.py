from scipy.optimize import minimize

class ConjugateGradient:

    METHOD_NAME = 'CG'

    def calculateOptimal(self,individual,function):
        return minimize(function.error,individual.genes,args=(0),method=self.METHOD_NAME).x 

    @classmethod
    def getMethod(cls):
        return cls()