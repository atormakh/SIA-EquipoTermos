import json
from optimizationMethods.gradientDescent import GradientDescent
from optimizationMethods.conjugateGradient import ConjugateGradient
from optimizationMethods.adam import Adam
from os import listdir
from os.path import isfile, join
from problemManager import ProblemManager
from epsilon import Epsilon

possibleOptimizationMethods = {'GD':GradientDescent, 'CG':ConjugateGradient, 'ADAM':Adam}

class ConfigHelper:

    MAX_INDIVIDUAL_SIZE = 11

    def __init__(self,configPath):
            # self.allValid = True
            # self.isMulti = False
            # self.allCategory = None
            with open(configPath,"r") as config_file:
                data = json.load(config_file)

                # ##Primero, chequeamos si se pidio la opcion de "ALL" o no
                # if('all' in data ):
                #     #En caso de pedirse, chequeamos que sea valida
                #     self.__checkAll(data['all'])
                #     #En caso de ser valida, se generan los configHelpers correspondientes
                #     if(self.allValid):
                #         self.isMulti = True
                #         self.multi = self.__getAll() 

                ##Pidiendo la seed para el random en caso de que se haya definido
                if('random_seed' in data):
                    self.randomSeed = data['random_seed']
                else:
                    self.randomSeed = None
                ##Pidiendo las propiedades del algoritmo de optimizacion
                #method
                if('method' in data['optimization_properties']):
                    self.method = data['optimization_properties']['method']
                else:
                    self.method = None
                #maxRangeGen
                if('max_range_gen' in data['optimization_properties']):
                    self.maxRangeGen = data['optimization_properties']['max_range_gen']
                else:
                    self.maxRangeGen = None
                # #stepSize
                # if('step_size' in data['optimization_properties']):
                #     self.stepSize = data['optimization_properties']['step_size']
                # else:
                #     self.stepSize = None
                #maxToleranceExponent
                if('max_tolerance_exponent' in data['optimization_properties']):
                    self.maxToleranceExponent = data['optimization_properties']['max_tolerance_exponent']
                else:
                    self.maxToleranceExponent = None

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
        return f"\t-Optimization method : {self.method}\n\t\t-Max tolerance exponent:{self.maxToleranceExponent}\n\t\t-Epsilon : {self.epsilon} \n\t\t-C : {self.c}"

    def __repr__(self) -> str:
        return self.__str__()

    def validateConfigurationProperties(self):
        return self.__validateRandomSeed() and self.__validateOptimizationProperties() and self.__validateProblemProperties()

    def __validateRandomSeed(self):
        if(self.randomSeed is not None and not (isinstance(self.randomSeed,int) or isinstance(self.randomSeed,float))):
            print("Illegal random seed : Should be a number")
            return False
        return True

    def __validateOptimizationProperties(self):
        return self.__validateMaxRangeGen() and self.__validateOptimizationMethod() and self.__validateMaxToleranceExponent()
    
    def __validateProblemProperties(self):
        return self.__validateEpsilon() and self.__validateC()

    def __validateMaxRangeGen(self):
        if(self.maxRangeGen is None):
            print(" 'max_range_gen' is a required parameter")
            return False
        isValid = isinstance(self.maxRangeGen,int) and self.maxRangeGen > 0
        if(not isValid):
            print("Illegal max range gen : Should be an integer positive number")
        return isValid

    def __validateOptimizationMethod(self):
        isValid = self.method is not None and isinstance(self.method,str)
        if(not isValid):
            print('It is required to determine a "method" in a form of a string.')
            return isValid
        optimizationMethodClass=self.getOptimizationMethodClass(self.method.strip().upper())
        if(optimizationMethodClass is None):
            print("Illegal optimization method used.")
            return False
        # (isValid,errorMessage)=crossMethodClass.isValid(self.crossData)
        # if not isValid:
        #     print(errorMessage) 
        return isValid

    def __validateMaxToleranceExponent(self):
        if(self.maxToleranceExponent is None):
            print(" 'max_tolerance_exponent' is a required parameter")
            return False
        isValid = isinstance(self.maxToleranceExponent,int) and self.maxToleranceExponent<0
        if(not isValid):
            print("Illegal max tolerance exponent : Should be an integer negative number (zero not included)")
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

    # def __checkAll(self,category):
    #     self.allValid = isinstance(category,str) and category.strip().upper() in possibleAllOptions
    #     if(self.allValid):
    #         self.allCategory = category.strip().lower()

    # def __getAll(self):
    #     onlyfiles = [f for f in listdir(f"./config/exampleConfigs/{self.allCategory}") if isfile(join(f"./config/exampleConfigs/{self.allCategory}", f))]
    #     helpers = []
    #     for file in onlyfiles:
    #         helpers.append(ConfigHelper(f"./config/exampleConfigs/{self.allCategory}/{file}"))

    #     return helpers

    # def getAllCategoryData(self,category):
    #     if(category is not None):
    #         categoryDataDict = {'cross':self.crossData,'mutation':self.mutationData,'selection':self.selectionData,'finish_condition':self.finishConditionData}
    #         return categoryDataDict.get(category)
    #     return None

    @staticmethod
    def getOptimizationMethodClass(method):
        return possibleOptimizationMethods.get(method)


