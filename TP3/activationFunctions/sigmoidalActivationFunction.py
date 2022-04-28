import numpy as np
class SigmoidalActivationFunction:

    def __init__(self):
        self.name = 'SIGMOIDAL'
    
    def apply(self,h):
        return 1 / (1 + np.exp(-h))

    def applyDerivative(self,h):
        return h * (1.0 - h)

    @classmethod
    def getType(cls):
        return cls()