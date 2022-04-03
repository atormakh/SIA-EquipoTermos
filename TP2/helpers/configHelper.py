import json
from selectionMethods.tournamentSelection import TournamentSelection
from crossingMethods.uniformCross import UniformCross
from crossingMethods.multipleCross import MultipleCross
from crossingMethods.simpleCross import SimpleCross
from selectionMethods.eliteSelection import EliteSelection
from selectionMethods.truncatedSelection import TruncatedSelection
from selectionMethods.rankSelection import RankSelection
from selectionMethods.rouletteSelection import RouletteSelection
from selectionMethods.boltzmannSelection import BoltzmannSelection
from mutationMethods.gaussianMutation import GaussianMutation
from mutationMethods.uniformMutation import UniformMutation
from finishConditions.generationSizeFinishCondition import GenerationSizeFinishCondition
from finishConditions.timeFinishCondition import TimeFinishCondition
from finishConditions.acceptableSolutionFinishCondition import AcceptableSolutionFinishCondition
from finishConditions.contentFinishCondition import ContentFinishCondition
from os import listdir
from os.path import isfile, join
from problemManager import ProblemManager
from epsilon import Epsilon

possibleSelectionMethods = {'ELITE':EliteSelection,'ROULETTE':RouletteSelection,'TOURNAMENTS':TournamentSelection,'BOLTZMANN':BoltzmannSelection,'TRUNCATED':TruncatedSelection ,'RANK':RankSelection}
possibleCrossMethods = {'SIMPLE':SimpleCross,'MULTIPLE':MultipleCross,'UNIFORM':UniformCross}
possibleMutationMethods = {'GAUSSIAN':GaussianMutation,'UNIFORM':UniformMutation}
possibleFinishConditions = {'GENERATION_SIZE':GenerationSizeFinishCondition, 'TIME':TimeFinishCondition, 'ACCEPTABLE_SOLUTION':AcceptableSolutionFinishCondition, 'CONTENT':ContentFinishCondition}
possibleAllOptions = ['CROSS','MUTATION','SELECTION','FINISH_CONDITION']

class ConfigHelper:


    MAX_INDIVIDUAL_SIZE = 11

    def __init__(self,configPath):
            self.allValid = True
            self.isMulti = False
            self.allCategory = None
            with open(configPath,"r") as config_file:
                data = json.load(config_file)

                ##Primero, chequeamos si se pidio la opcion de "ALL" o no
                if('all' in data ):
                    #En caso de pedirse, chequeamos que sea valida
                    self.__checkAll(data['all'])
                    #En caso de ser valida, se generan los configHelpers correspondientes
                    if(self.allValid):
                        self.isMulti = True
                        self.multi = self.__getAll() 

                ##Pidiendo la seed para el random en caso de que se haya definido
                if('random_seed' in data):
                    self.randomSeed = data['random_seed']
                else:
                    self.randomSeed = None
                ##Pidiendo las propiedades del algoritmo genetico 
                #populationSize
                if('population_size' in data['genetic_properties']):
                    self.populationSize = data['genetic_properties']['population_size']
                else:
                    self.populationSize = None
                #maxRangeGen
                if('max_range_gen' in data['genetic_properties']):
                    self.maxRangeGen = data['genetic_properties']['max_range_gen']
                else:
                    self.maxRangeGen = None
                #replacement
                if('replacement' in data['genetic_properties']):
                    self.replacement = data['genetic_properties']['replacement']
                else:
                    self.replacement = None
                #cross  
                if('cross' in data['genetic_properties'] and 'method' in data['genetic_properties']['cross']):
                    self.crossData = data['genetic_properties']['cross']
                else:
                    self.crossData = None
                #selection
                if('selection' in data['genetic_properties'] and 'method' in data['genetic_properties']['selection']):
                    self.selectionData = data['genetic_properties']['selection']
                else:
                    self.selectionData = None
                #mutation
                if('mutation' in data['genetic_properties'] and 'method' in data['genetic_properties']['mutation']):
                    self.mutationData = data['genetic_properties']['mutation']
                else:
                    self.mutationData = None
                #finishCondition
                if('finish_condition' in data['genetic_properties'] and 'method' in data['genetic_properties']['finish_condition']):
                    self.finishConditionData = data['genetic_properties']['finish_condition']
                else:
                    self.finishConditionData = None

                ##Pidiendo las propiedades del problema
                #epsilon
                if('epsilon' in data['problem_properties']):
                    reactives = list(data['problem_properties']['epsilon'].values())
                    self.epsilon = Epsilon(reactives)
                else:
                    self.epsilon = None
                #c
                if('c' in data['problem_properties']):
                    self.c = data['problem_properties']['c']
                else:
                    self.c = None

    def __str__(self):
        return f"\t-Poblation size : {self.populationSize}\n\t\t-Finish Condition:{self.finishConditionData}\n\t\t-Cross method : {self.crossData} \n\t\t-Mutation : {self.mutationData}\n\t\t-Selection Data : {self.selectionData}"

    def __repr__(self) -> str:
        return self.__str__()

    def validateConfigurationProperties(self):
        return self.__validateRandomSeed() and self.__validateGeneticProperties() and self.__validateProblemProperties()

    def __validateRandomSeed(self):
        if(self.randomSeed is not None and not (isinstance(self.randomSeed,int) or isinstance(self.randomSeed,float))):
            print("Illegal random seed : Should be a number")
            return False
        return True

    def __validateGeneticProperties(self):
        return self.__validatePopulationSize() and self.__validateMaxRangeGen() and self.__validateReplacement() and self.__validateCrossMethod() and self.__validateMutationMethod() and self.__validateSelectionMethod() and self.__validateFinishCondition()

    def __validateProblemProperties(self):
        return self.__validateEpsilon() and self.__validateC()

    def __validatePopulationSize(self):
        if(self.populationSize is None):
            print(" 'population_size' is a required parameter")
            return False
        isValid = isinstance(self.populationSize,int) and self.populationSize > 1
        if(not isValid):
            print("Illegal population size : Should be an integer positive number and greater than 1")
        return isValid

    def __validateMaxRangeGen(self):
        if(self.maxRangeGen is None):
            print(" 'max_range_gen' is a required parameter")
            return False
        isValid = isinstance(self.maxRangeGen,int) and self.maxRangeGen > 0
        if(not isValid):
            print("Illegal max range gen : Should be an integer positive number")
        return isValid

    def __validateReplacement(self):
        if(self.replacement is None):
            print(" 'replacement' is a required parameter")
            return False
        isValid = isinstance(self.replacement,bool)
        if(not isValid):
            print("Illegal replacement : Should be a boolean value (true or false)")
        return isValid

    def __validateCrossMethod(self):
        isValid = self.crossData is not None and isinstance(self.crossData["method"],str)
        if(not isValid):
            print('It is required to determine a "crossMethod" in a form of a string.')
            return isValid
        crossMethodClass=self.getCrossMethodClass(self.crossData["method"].strip().upper())
        if(crossMethodClass is None):
            print("Illegal cross method used.")
            return False
        (isValid,errorMessage)=crossMethodClass.isValid(self.crossData)
        if not isValid:
            print(errorMessage) 
        return isValid

    def __validateMutationMethod(self):
        isValid = self.mutationData is not None and isinstance(self.mutationData["method"],str)
        if(not isValid):
            print(" 'mutationMethod' is a required parameter. Also it must be a string")
            return isValid
        mutationMethodClass=self.getMutationMethodClass(self.mutationData["method"].strip().upper())
        if(mutationMethodClass is None):
            print("Illegal mutation method used.")
            return False
        (isValid,errorMessage)=mutationMethodClass.isValid(self.mutationData)
        if not isValid:
            print(errorMessage) 
        return isValid

    def __validateSelectionMethod(self):
        isValid = self.selectionData is not None and isinstance(self.selectionData["method"],str)
        if(not isValid):
            print(" 'selectionMethod' is a required parameter. Also it must be a string")
            return isValid
        selectionMethodClass = self.getSelectionMethodClass(self.selectionData["method"].strip().upper())
        if(selectionMethodClass is None):
            print("Illegal selection method used")
            return False
        (isValid,errorMessage)= selectionMethodClass.isValid(self.selectionData,self.populationSize)
        if not isValid:
            print(errorMessage) 
        return isValid

    def __validateFinishCondition(self):
        isValid = self.finishConditionData is not None and isinstance(self.finishConditionData["method"],str)
        if(not isValid):
            print(" 'finishConditionMethod' is a required parameter. Also it must be a string")
            return False
        finishConditionClass = self.getFinishConditionClass(self.finishConditionData["method"].strip().upper())
        if(finishConditionClass is None):
            print("Illegal finish condition used")
            return False
        (isValid,errorMessage)= finishConditionClass.isValid(self.finishConditionData)
        if not isValid:
            print(errorMessage) 
        return isValid

    def __validateEpsilon(self):
        if(self.epsilon is None):
            print(" 'epsilon' is a required parameter.")
            return False
        problemManager = ProblemManager(self.epsilon,self.c)
        isValid = problemManager.validateEpsilon()
        if(not isValid):
            print("Illegal epsilon")
        return isValid

    def __validateC(self):
        if(self.c is None):
            print(" 'c' is a required parameter.")
            return False
        problemManager = ProblemManager(self.epsilon,self.c)
        isValid = problemManager.validateC()
        if(not isValid):
            print("Illegal C")
        return isValid

    def __checkAll(self,category):
        self.allValid = isinstance(category,str) and category.strip().upper() in possibleAllOptions
        if(self.allValid):
            self.allCategory = category.strip().lower()

    def __getAll(self):
        onlyfiles = [f for f in listdir(f"./config/exampleConfigs/{self.allCategory}") if isfile(join(f"./config/exampleConfigs/{self.allCategory}", f))]
        helpers = []
        for file in onlyfiles:
            helpers.append(ConfigHelper(f"./config/exampleConfigs/{self.allCategory}/{file}"))

        return helpers

    def getAllCategoryData(self,category):
        if(category is not None):
            categoryDataDict = {'cross':self.crossData,'mutation':self.mutationData,'selection':self.selectionData,'finish_condition':self.finishConditionData}
            return categoryDataDict.get(category)
        return None

    @staticmethod
    def getSelectionMethodClass(method):
        return possibleSelectionMethods.get(method)

    @staticmethod
    def getCrossMethodClass(method):
        return possibleCrossMethods.get(method)

    @staticmethod
    def getMutationMethodClass(method):
        return possibleMutationMethods.get(method)

    @staticmethod
    def getFinishConditionClass(method):
        return possibleFinishConditions.get(method)


