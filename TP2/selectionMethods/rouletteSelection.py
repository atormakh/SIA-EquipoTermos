import py_compile
import numpy as np
import random

class RouletteSelection:

    def __init__(self):
        print("Corre roulette")

    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        #Sacamos el fitness total
        #return random.choices(selectionIndividuals , weights=[x.fitness for x in selectionIndividuals] , k=targetPopulationSize )
        totalFitness = sum(ind.fitness for ind in selectionIndividuals)
        accumulatedProb = 0
        probArray = []
        for ind in selectionIndividuals:
            #Obtenemos la probabilidad acumulada de cada individuo
            prob = ind.fitness
            accumulatedProb+= prob

            probArray.append( (accumulatedProb , ind ) )

        selectedPopulation = []   

        for i in range(0 , targetPopulationSize):
            selectedPopulation.append(self.__runRoulette(probArray , totalFitness))

        return selectedPopulation

    def __runRoulette(self , probArray , totalFitness):
        prob = np.random.uniform(0 , totalFitness)
        for ind in probArray:
            if(prob <= ind[0]):
                return ind[1]
        return probArray[-1][1]

    @classmethod
    def fromJson(cls,selectionData):
        return cls()

    @staticmethod
    def isValid(selectionData,populationSize=None):
        return (True,"")


