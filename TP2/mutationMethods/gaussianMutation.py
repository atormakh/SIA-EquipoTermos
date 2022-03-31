import numpy as np
import random

class GaussianMutation:

    def __init__(self,p,sigma):
        self.p=p
        self.sigma=sigma

    def apply(self,individual):
        for i in range(0,len(individual.genes)):
            if(self.p >= random.random()):
                individual.genes[i] +=np.random.normal(0,self.sigma)

    @classmethod
    def fromJson(cls, mutationData):
        return cls(mutationData['probability'],mutationData['sigma'])

    @staticmethod
    def isValid(mutationData):
        isValid = True
        errorMessage = ""
        probability = None
        if('probability' in mutationData):
            probability = mutationData['probability']
        if(probability is None or not isinstance(probability,float) or probability < 0 or probability > 1):
            isValid = False
            errorMessage = "Invalid Gaussian Mutation parameters. 'probability' is a required parameter and it must be a decimal number between 0 and 1 (limits included)"
        sigma = None
        if('sigma' in mutationData):
            sigma = mutationData['sigma']
        if(sigma is None or not isinstance(sigma,float) or sigma < 0):
            isValid = False
            errorMessage = "Invalid Gaussian Mutation parameters. 'sigma' is a required parameter and it must be positive decimal number"
        return (isValid,errorMessage)
