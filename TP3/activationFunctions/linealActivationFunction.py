import numpy as np
class LinealActivationFunction:

    def __init__(self):
        self.name = 'LINEAL'
    
    def apply(self,h):
        return h

    def applyDerivative(self,h):
        return np.full(np.shape(h),1.0)

    @classmethod
    def getType(cls):
        return cls()