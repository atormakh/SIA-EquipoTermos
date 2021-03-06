import py_compile
import numpy as np
import random

class RankSelection:

    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        #Ordenamos los individuos por fitness
        rankedIndividuals = sorted(selectionIndividuals,key=lambda x: x.fitness,reverse=True)
        p = len(rankedIndividuals)

        valueRankedIndividuals = []
        rankValueAcum = 0
        #Genero un ranking acumulado dependiendo de la posicion en el vector de rango
        for idx , individual in enumerate(rankedIndividuals):

            rankValue = (p - (idx + 1 )) / p
            rankValueAcum += rankValue
            valueRankedIndividuals.append((rankValueAcum , individual))
            
        selectedPopulation = []   
        #Tiro la ruleta la cantidad de veces necesarias
        for i in range(0 , targetPopulationSize):
            selectedPopulation.append(self.__runRoulette(valueRankedIndividuals,rankValueAcum))

        return selectedPopulation

    def __runRoulette(self , rankArray , maxValue):
        rank = np.random.uniform(0 , maxValue)
        for ind in rankArray:
            if(rank <= ind[0]):
                return ind[1]
        return rankArray[-1][1]

    @classmethod
    def fromJson(cls,selectionData):
        return cls()

    @staticmethod
    def isValid(selectionData,populationSize=None):
        return (True,"")


