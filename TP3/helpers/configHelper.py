import json
from activationFunctions.stepActivationFunction import StepActivationFunction
from activationFunctions.linealActivationFunction import LinealActivationFunction
from activationFunctions.hyperbolicTangentActivationFunction import HyperbolicTangentActivationFunction
from activationFunctions.sigmoidalActivationFunction import SigmoidalActivationFunction
from os import listdir
from os.path import isfile, join

possibleActivationFunctionTypes = {'STEP':StepActivationFunction,'LINEAL':LinealActivationFunction,'TANH':HyperbolicTangentActivationFunction,'SIGMOIDAL':SigmoidalActivationFunction}

class ConfigHelper:

    def __init__(self,configPath):
            with open(configPath,"r") as config_file:
                data = json.load(config_file)

                ##Pidiendo las propiedades de la red neuronal
                #architecture
                if('architecture' in data['neural_net']):
                    self.architecture = data['neural_net']['architecture']
                else:
                    self.architecture = None
                #activationFunction
                if('activation_function' in data['neural_net'] and 'type' in data['neural_net']['activation_function']):
                    self.activationFunctionType = data['neural_net']['activation_function']['type']
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


    def validateConfigurationProperties(self):
        return self.__validateNeuralNetProperties() and self.__validateBacktrackingProperties() and self.__validateMaxIterations()

    def __validateNeuralNetProperties(self):
        return self.__validateArchitecture() and self.__validateActivationFunctionType()

    def __validateBacktrackingProperties(self):
        return self.__validateLearningRate()

    def __validateMaxIterations(self):
        if(self.maxIterations is None):
            print(" 'max_iterations' is a required parameter")
            return False
        isValid = isinstance(self.maxIterations,int) and self.maxIterations > 0
        if(not isValid):
            print("Illegal max iterations : Should be an integer positive number")
        return isValid

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
        isValid = isinstance(self.architecture,list) and len(self.architecture)>=2 and all((isinstance(x, int) and x>0) for x in self.architecture) and self.architecture[len(self.architecture)-1]==1
        if(not isValid):
            print("Illegal architecture : Should be an array of integer positive numbers, with length greater or equal than 2 and with his last item equal to 1")
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

    @staticmethod
    def getActivationFunctionClass(type):
        return possibleActivationFunctionTypes.get(type)


