import json
from selectionMethods.tournamentSelection import TournamentSelection
from crossingMethods.uniformCross import UniformCross
from crossingMethods.multipleCross import MultipleCross
from crossingMethods.simpleCross import SimpleCross
from selectionMethods.eliteSelection import EliteSelection
from selectionMethods.truncatedSelection import TruncatedSelection
from problemManager import ProblemManager
from mutation import Mutation
from epsilon import Epsilon
possibleSelectionMethods = {'ELITE':EliteSelection,'ROULETTE':None,'TOURNAMENTS':TournamentSelection,'BOLTZMANN':None,'TRUNCATED':TruncatedSelection}
possibleCrossMethods = {'SIMPLE':SimpleCross,'MULTIPLE':MultipleCross,'UNIFORM':UniformCross}
class ConfigHelper:


    MAX_INDIVIDUAL_SIZE = 11

    def __init__(self,configPath):
            with open(configPath,"r") as config_file:
                data = json.load(config_file)
                ##Pidiendo las propiedades del algoritmo genetico 
                self.populationSize = data['genetic_properties']['population_size']
                self.maxGenerationSize = data['genetic_properties']['max_generation_size']
                self.crossData = data['genetic_properties']['cross']
                mutationProbability = data['genetic_properties']['mutation']['probability']
                mutationSigma = data['genetic_properties']['mutation']['sigma']
                self.mutation = Mutation(mutationProbability,mutationSigma)
                self.selectionData = data['genetic_properties']['selection']

                ##Pidiendo las propiedades del problema
                reactives = list(data['problem_properties']['epsilon'].values())
                self.epsilon = Epsilon(reactives)
                self.c = data['problem_properties']['c']

    def __str__(self):
        return f"\t-Poblation size : {self.poblationSize}\n\t-Max generation size : {self.maxGenerationSize}\n\t-Cross method : {self.crossMethod}\n\t-Mutation : [ p : {self.mutation.p} ; sigma : {self.mutation.sigma} ]\n\t-Selection Data : {self.selectionData}"

    def __repr__(self) -> str:
        return self.__str__()

    def validateConfigurationProperties(self):
        return self.__validateGeneticProperties() and self.__validateProblemProperties()

    def __validateGeneticProperties(self):
        return self.__validatePopulationSize() and self.__validateMaxGenerationSize() and self.__validateCrossMethod() and self.__validateMutation() and self.__validateSelectionMethod()

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
        isValid = self.crossData is not None and isinstance(self.crossData["method"],str)
        if(not isValid):
            print('It is required to determine a "crossMethod" in a form of a string.')
            return isValid
        crossMethodClass=self.getCrossMethodClass(self.crossData["method"].strip().upper())
        if(crossMethodClass is None):
            print("Illegal cross method used.")
        (isValid,errorMessage)=crossMethodClass.isValid(self.crossData)
        if not isValid:
            print(errorMessage) 
        return isValid

    def __validateMutation(self):
        probabilityValid = isinstance(self.mutation.p,float) and self.mutation.p >=0 and self.mutation.p <=1
        sigmaValid = isinstance(self.mutation.sigma,float) and self.mutation.sigma >=0
        isValid = probabilityValid and sigmaValid
        if(not isValid):
            print('Illegal mutation : Probability should be a decimal number between 0 and 1, and sigma should be positive decimal number')
        return isValid

    def __validateSelectionMethod(self):
        isValid = self.selectionData is not None and isinstance(self.selectionData["method"],str)
        if(not isValid):
            print(" 'selectionMethod' is a required parameter. Also it must be a string")
        selectionMethodClass = self.getSelectionMethodClass(self.selectionData["method"])
        if(selectionMethodClass is None):
            print("Illegal selection method used")
        (isValid,errorMessage)= selectionMethodClass.isValid(self.selectionData)
        if not isValid:
            print(errorMessage) 
        return isValid

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

    @staticmethod
    def getSelectionMethodClass(method):
        return possibleSelectionMethods[method]

    @staticmethod
    def getCrossMethodClass(method):
        return possibleCrossMethods[method]


