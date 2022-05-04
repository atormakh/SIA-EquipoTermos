import numpy as np
class SigmoidalActivationFunction:

    def __init__(self,beta):
        self.name = 'SIGMOIDAL'
        self.beta = beta
    
    def apply(self,h):
        return 1 / (1 + np.exp(np.multiply(-2*self.beta,h)))

    def applyDerivative(self,h):

        oneArray = np.full(np.shape(h),1.0)
        return np.multiply(np.multiply(2*self.beta,self.apply(h)),np.subtract(oneArray,self.apply(h)))

    @classmethod
    def getType(cls,beta=1):
        if beta is None:
            beta=1
        return cls(beta)