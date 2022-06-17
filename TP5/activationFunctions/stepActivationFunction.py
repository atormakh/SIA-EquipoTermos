import numpy as np
class StepActivationFunction:

    def __init__(self):
        self.name = 'STEP'

    def apply(self,h):
        
        step = lambda e: -1 if e<0 else 1 
            
        return np.vectorize(step)(h)

    def applyDerivative(self,h):
        return np.full(np.shape(h),1.0)

    @classmethod
    def getType(cls,beta=1):
        return cls()

    