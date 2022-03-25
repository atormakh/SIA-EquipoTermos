import numpy as np
import random

class Mutation:
    def __init__(self,p,sigma):
        self.p=p
        self.sigma=sigma
    
    def apply(self,individual):
        for i in range(0,len(individual.genes)):
            if(self.p >= random.random()):
                individual.genes[i] +=np.random.normal(0,self.sigma) 
