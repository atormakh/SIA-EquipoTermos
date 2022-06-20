import numpy as np
class ReluActivationFunction:

    def __init__(self):
        self.name = 'RELU'
        self.beta = None

    def apply(self,h):
        
        step = lambda e: 0 if e<=0 else e
            
        return np.vectorize(step)(h)

    def applyDerivative(self,h):
        return np.full(np.shape(h),1.0)

    @classmethod
    def getType(cls,beta=1):
        return cls()
