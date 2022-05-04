import numpy as np
class HyperbolicTangentActivationFunction:

    def __init__(self,beta):
        self.name = 'TANH'
        self.beta = beta
    
    def apply(self,h):
        return np.tanh(np.multiply(self.beta,h))

    def applyDerivative(self,h):
        pow = lambda e: e**2
        oneArray = np.full(np.shape(h),1.0)
        return np.multiply(self.beta,np.subtract(oneArray,np.vectorize(pow)(self.apply(h))))

    @classmethod
    def getType(cls,beta):
        if beta is None:
            beta=1
        return cls(beta)