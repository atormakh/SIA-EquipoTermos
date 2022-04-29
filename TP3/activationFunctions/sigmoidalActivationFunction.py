import numpy as np
class SigmoidalActivationFunction:

    def __init__(self):
        self.name = 'SIGMOIDAL'
    
    def apply(self,h):
        return 1 / (1 + np.exp(-h))

    def applyDerivative(self,h):

        oneArray = np.full(np.shape(h),1.0)
        return np.multiply(self.apply(h),np.subtract(oneArray,self.apply(h)))

    @classmethod
    def getType(cls):
        return cls()