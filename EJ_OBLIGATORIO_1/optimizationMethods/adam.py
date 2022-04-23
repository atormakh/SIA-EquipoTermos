from autograd.misc.optimizers import adam
import numdifftools as nd
import numpy as np

class Adam:

    def __init__(self):
        self.useGeneralAlgorithm = False

    def calculateOptimal(self,individual,function):
        return adam(nd.Gradient(function.error),np.array(individual.genes),step_size=0.80085)

    def calculateDirection(self,individual):
        return None

    @classmethod
    def getMethod(cls):
        return cls()