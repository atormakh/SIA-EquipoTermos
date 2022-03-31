import numpy as np
import random

class UniformMutation:

    def __init__(self,p,a):
        self.p=p
        self.a=a

    def apply(self,individual):
        for i in range(0,len(individual.genes)):
            if(self.p >= random.random()):
                individual.genes[i] +=np.random.uniform(-self.a,self.a)

    @classmethod
    def fromJson(cls, mutationData):
        return cls(mutationData['probability'],mutationData['a'])

    @staticmethod
    def isValid(mutationData):
        isValid = True
        errorMessage = ""
        probability = None
        if('probability' in mutationData):
            probability = mutationData['probability']
        if(probability is None or not isinstance(probability,float) or probability < 0 or probability > 1):
            isValid = False
            errorMessage = "Invalid Uniform Mutation parameters. 'probability' is a required parameter and it must be a decimal number between 0 and 1 (limits included)"
        a = None
        if('a' in mutationData):
            a = mutationData['a']
        if(a is None or not isinstance(a,float) or a <= 0):
            isValid = False
            errorMessage = "Invalid Uniform Mutation parameters. 'a' is a required parameter and it must be positive decimal number (zero not included)"
        return (isValid,errorMessage)