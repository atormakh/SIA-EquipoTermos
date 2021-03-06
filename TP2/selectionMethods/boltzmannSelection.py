import py_compile
import numpy as np
import random

class BoltzmannSelection:

    def __init__(self , T0 , Tc , k):
        self.generation = 0
        self.initialT = T0
        self.finalT = Tc
        self.k = k


    #Funcion de temperatura dada en clase
    def __temperature(self):
        return self.finalT + (self.initialT - self.finalT) * np.exp( - self.k * self.generation )
        
    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        valuedIndividuals = []
        total = 0
        #Por cada individuo calculo su valor (el dividendo de la probabilidad)
        for individual in selectionIndividuals:
            value = np.exp(individual.fitness / self.__temperature())
            total += value
            valuedIndividuals.append((value, individual))


        acumulated = 0
        promediatedIndividuals = []
        #Divido por el total para que la suma de probabilidades de 1 y les asigno la probabilidad acumulada
        for valuedIndividual in valuedIndividuals:
            acumulated+= valuedIndividual[0] / total
            promediatedIndividuals.append((acumulated , valuedIndividual[1]))

        selectedPopulation = []   
        #tiro la ruleta
        for i in range(0 , targetPopulationSize):
            selectedPopulation.append(self.__runRoulette(promediatedIndividuals,1))

        self.generation+= 1

        return selectedPopulation

    def __runRoulette(self , array , maxValue):
        selection = np.random.uniform(0 , maxValue)
        for ind in array:
            if(selection <= ind[0]):
                return ind[1]
        return array[-1][1]

    @classmethod
    def fromJson(cls,selectionData):
        return cls(selectionData["T0"] ,selectionData["Tc"] , selectionData["k"])

    @staticmethod
    def isValid(selectionData,PopulationSize = None):
        parameters = [ "T0" , "Tc" , "k"]
        for parameter in parameters:
            if(parameter not in selectionData):
                return (False , "Missing parameter: " + parameter)
            if(not (isinstance(selectionData[parameter],(int , float)))):
                return (False , "Parameter " + parameter + "should be of float or int type but it is of type " + type(parameter).__name__)
            if( selectionData[parameter] < 0):
                return (False , parameter + " must be a positive value")


        if(selectionData["T0"] < selectionData["Tc"]):
            return (False , "T0 should be greater or equal to Tc")
        if(selectionData["k"] < 0 or selectionData["k"] > 1 ):
            return(False , "k should be a value between 0 and 1")
        return (True,"")






