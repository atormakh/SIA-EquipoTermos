import numpy as np
class HyperbolicTangentActivationFunction:

    def __init__(self):
        self.name = 'TANH'
    
    def apply(self,h):
        return np.tanh(h)

    def applyDerivative(self,h):
        pow = lambda e: e**2 
        return 1.0 - np.vectorize(pow)(np.tanh(h))

    @classmethod
    def getType(cls):
        return cls()