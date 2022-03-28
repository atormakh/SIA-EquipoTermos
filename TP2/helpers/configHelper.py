import json
from os import listdir
from os.path import isfile, join
from problemManager import ProblemManager
from mutation import Mutation
from epsilon import Epsilon

class ConfigHelper:

    possibleSelectionMethods = tuple(['ELITE','ROULETTE','TOURNAMENTS','BOLTZMANN','TRUNCATED'])
    possibleCrossMethods = tuple(['SIMPLE','MULTIPLE','UNIFORM'])
    MAX_INDIVIDUAL_SIZE = 11

    def __init__(self,configPath):
            with open(configPath,"r") as config_file:
                data = json.load(config_file)
                ##Pidiendo las propiedades del algoritmo genetico 
                self.populationSize = data['genetic_properties']['population_size']
                self.maxGenerationSize = data['genetic_properties']['max_generation_size']
                self.crossMethod = data['genetic_properties']['cross_method']
                if 'cross_index_count' in data['genetic_properties']:
                    self.crossIndexCount = data['genetic_properties']['cross_index_count']
                else:
                    self.crossIndexCount = None
                mutationProbability = data['genetic_properties']['mutation']['probability']
                mutationSigma = data['genetic_properties']['mutation']['sigma']
                self.mutation = Mutation(mutationProbability,mutationSigma)
                self.selectionMethod = data['genetic_properties']['selection_method']

                ##Pidiendo las propiedades del problema
                reactives = list(data['problem_properties']['epsilon'].values())
                self.epsilon = Epsilon(reactives)
                self.c = data['problem_properties']['c']

    def __str__(self):
        return f"\t-Poblation size : {self.poblationSize}\n\t-Max generation size : {self.maxGenerationSize}\n\t-Cross method : {self.crossMethod}\n\t-Mutation : [ p : {self.mutation.p} ; sigma : {self.mutation.sigma} ]\n\t-Selection method : {self.selectionMethod}"

    def __repr__(self) -> str:
        return self.__str__()

    def validateConfigurationProperties(self):
        return self.__validateGeneticProperties() and self.__validateProblemProperties()

    def __validateGeneticProperties(self):
        return self.__validatePopulationSize() and self.__validateMaxGenerationSize() and self.__validateCrossMethod() and self.__validateCrossIndexCount() and self.__validateMutation() and self.__validateSelectionMethod() and self.__validateRequiredParameters()

    def __validateProblemProperties(self):
        return self.__validateEpsilon() and self.__validateC()

    def __validatePopulationSize(self):
        isValid = isinstance(self.populationSize,int) and self.populationSize > 0
        if(not isValid):
            print("Illegal population size : Should be an integer positive number")
        return isValid
    
    def __validateMaxGenerationSize(self):
        isValid = isinstance(self.maxGenerationSize,int) and self.maxGenerationSize > 0
        if(not isValid):
            print("Illegal max generation size : Should be an integer positive number")
        return isValid

    def __validateCrossMethod(self):
        isValid = isinstance(self.crossMethod,str) and self.crossMethod.strip().upper() in self.possibleCrossMethods
        if(not isValid):
            print('Illegal cross method used')
        return isValid

    def __validateCrossIndexCount(self):
        if self.crossIndexCount is not None:
            isValid = isinstance(self.crossIndexCount,int) and self.crossIndexCount >=2 and self.crossIndexCount<=self.MAX_INDIVIDUAL_SIZE
            if(not isValid):
                print('Illegal cross index count : Should be an integer number between 2 and '+str(self.MAX_INDIVIDUAL_SIZE)+' (limits included)')
            return isValid
        return True

    def __validateMutation(self):
        probabilityValid = isinstance(self.mutation.p,float) and self.mutation.p >=0 and self.mutation.p <=1
        sigmaValid = isinstance(self.mutation.sigma,float) and self.mutation.sigma >=0
        isValid = probabilityValid and sigmaValid
        if(not isValid):
            print('Illegal mutation : Probability should be a decimal number between 0 and 1, and sigma should be positive decimal number')
        return isValid

    def __validateSelectionMethod(self):
        isValid = isinstance(self.selectionMethod,str) and self.selectionMethod.strip().upper() in self.possibleSelectionMethods
        if(not isValid):
            print('Illegal selection method used')
        return isValid

    def __validateRequiredParameters(self):
        if self.crossMethod.strip().upper() == 'MULTIPLE':
            isValid = self.crossIndexCount is not None
            if(not isValid):
                print('An index count is required to this cross method, add the field \"cross_index_count\" into your genetic options')
            return isValid
        return True

    def __validateEpsilon(self):
        problemManager = ProblemManager(self.epsilon,self.c)
        isValid = problemManager.validateEpsilon()
        if(not isValid):
            print("Illegal epsilon")
        return isValid

    def __validateC(self):
        problemManager = ProblemManager(self.epsilon,self.c)
        isValid = problemManager.validateC()
        if(not isValid):
            print("Illegal C")
        return isValid


