import json
from activationFunctions.stepActivationFunction import StepActivationFunction
from activationFunctions.linealActivationFunction import LinealActivationFunction
from activationFunctions.hyperbolicTangentActivationFunction import HyperbolicTangentActivationFunction
from activationFunctions.sigmoidalActivationFunction import SigmoidalActivationFunction
from os import listdir
from os.path import isfile, join

possibleActivationFunctionTypes = {'STEP':StepActivationFunction,'LINEAL':LinealActivationFunction,'TANH':HyperbolicTangentActivationFunction,'SIGMOIDAL':SigmoidalActivationFunction}

class ConfigHelper:

    DEFAULT_BETA = 1

    def __init__(self,configPath):
            with open(configPath,"r") as config_file:

                data = json.load(config_file)

                ##Pidiendo las propiedades de la red neuronal
                #architecture
                if('architecture' in data['neural_net']):
                    self.architecture = data['neural_net']['architecture']
                else:
                    self.architecture = None
                #activationFunction (type y beta si este ultimo fue especificado)
                
                if('activation_function' in data['neural_net'] and 'beta' in data['neural_net']['activation_function']):
                    self.beta = data['neural_net']['activation_function']['beta']
                else:
                    self.beta = None

                if('activation_function' in data['neural_net'] and 'type' in data['neural_net']['activation_function']):
                    self.activationFunctionType = data['neural_net']['activation_function']['type']
                    self.activationFunctionClass = self.getActivationFunctionClass(self.activationFunctionType.strip().upper()).getType(self.beta)
                else:
                    self.activationFunctionType = None
                
                ##Pidiendo las propiedades de backtracking
                #learningRate
                if('learning_rate' in data['backtracking']):
                    self.learningRate = data['backtracking']['learning_rate']
                else:
                    self.learningRate = None

                ##Pidiendo las propiedades del problema en general
                #maxIterations
                if('max_iterations' in data):
                    self.maxIterations = data['max_iterations']
                else:
                    self.maxIterations = None
                #maxToleranceExponent
                if('max_tolerance_exponent' in data):
                    self.maxToleranceExponent = data['max_tolerance_exponent']
                else:
                    self.maxToleranceExponent = None
                ##randomSeed
                if('random_seed' in data):
                    self.randomSeed = data['random_seed']
                else:
                    self.randomSeed = None
                
            #Finalmente, le asignamos una propiedad que indique si las anteriores leidas son validas o no
            self.isValid = self.validateConfigurationProperties()
        


    def __str__(self):
        return f"\t-Architecture : {self.architecture}\n\t\t-Activation function :{self.activationFunctionType}\n\t\t-Beta : {self.beta}\n\t\t-Learning rate : {self.learningRate} \n\t\t-Max iterations : {self.maxIterations}\n\t\t-Error bound : 1e^{self.maxToleranceExponent}"

    def __repr__(self) -> str:
        return self.__str__()

    def getProperties(self):
        return (self.architecture,self.activationFunctionClass,self.beta,self.learningRate,self.maxIterations,self.maxToleranceExponent)

    def validateConfigurationProperties(self):
        return self.__validateNeuralNetProperties() and self.__validateBacktrackingProperties() and self.__validateGeneralProperties()

    def __validateNeuralNetProperties(self):
        return self.__validateArchitecture() and self.__validateActivationFunctionType() and self.__validateBeta()

    def __validateBacktrackingProperties(self):
        return self.__validateLearningRate()

    def __validateGeneralProperties(self):
        return self.__validateMaxIterations() and self.__validateMaxToleranceExponent() and self.__validateRandomSeed()

    def __validateLearningRate(self):
        if(self.learningRate is None):
            print(" 'learning_rate' is a required parameter")
            return False
        isValid = (isinstance(self.learningRate,float) and self.learningRate > 0 and self.learningRate<=1) or (isinstance(self.learningRate,int) and self.learningRate==1)
        if(not isValid):
            print("Illegal learning rate : Should be a positive decimal number between 0 and 1 (zero excluded, one included)")
        return isValid

    def __validateArchitecture(self):
        if(self.architecture is None):
            print(" 'architecture' is a required parameter")
            return False
        isValid = isinstance(self.architecture,list) and len(self.architecture)>=2 and all((isinstance(x, int) and x>0) for x in self.architecture)
        if(not isValid):
            print("Illegal architecture : Should be an array of integer positive numbers, with length greater or equal than 2")
        return isValid

    def __validateActivationFunctionType(self):
        isValid = self.activationFunctionType is not None and isinstance(self.activationFunctionType,str)
        if(not isValid):
            print('It is required to determine a "activationFunctionType" in a form of a string.')
            return isValid
        activationFunctionClass=self.getActivationFunctionClass(self.activationFunctionType.strip().upper())
        if(activationFunctionClass is None):
            print("Illegal activation function used")
            return False
        return isValid

    def __validateBeta(self):
        if(self.beta is None):
            self.beta = self.DEFAULT_BETA
            return True
        isValid = (isinstance(self.beta,float) and self.beta > 0 and self.beta<=1) or (isinstance(self.beta,int) and self.beta==1)
        if(not isValid):
            print("Illegal beta : Should be a positive decimal number between 0 and 1 (zero excluded, one included)")
        return isValid

    def __validateMaxIterations(self):
        if(self.maxIterations is None):
            print(" 'max_iterations' is a required parameter")
            return False
        isValid = isinstance(self.maxIterations,int) and self.maxIterations > 0
        if(not isValid):
            print("Illegal max iterations : Should be an integer positive number")
        return isValid

    def __validateMaxToleranceExponent(self):
        if(self.maxToleranceExponent is None):
            print(" 'max_tolerance_exponent' is a required parameter")
            return False
        isValid = isinstance(self.maxToleranceExponent,int) and self.maxToleranceExponent < 0
        if(not isValid):
            print("Illegal max tolerance exponent : Should be an negative  number (zero not included)")
        return isValid

    def __validateRandomSeed(self):
        if(self.randomSeed is not None and not isinstance(self.randomSeed,int)):
            print("Illegal random seed : Should be an integer number")
            return False
        return True

    @staticmethod
    def getActivationFunctionClass(type):
        return possibleActivationFunctionTypes.get(type)


