import imp
import json
from activationFunctions.stepActivationFunction import StepActivationFunction
from activationFunctions.linealActivationFunction import LinealActivationFunction
from activationFunctions.hyperbolicTangentActivationFunction import HyperbolicTangentActivationFunction
from activationFunctions.sigmoidalActivationFunction import SigmoidalActivationFunction
from activationFunctions.reluActivationFunction import ReluActivationFunction
from os import listdir
from os.path import isfile, join

possibleActivationFunctionTypes = {'STEP':StepActivationFunction,'LINEAL':LinealActivationFunction,'TANH':HyperbolicTangentActivationFunction,'SIGMOIDAL':SigmoidalActivationFunction,'RELU':ReluActivationFunction}
possibleFonts = ['FONT1','FONT2','FONT3']

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

                # #activationFunction (type y beta si este ultimo fue especificado)
                # if('activation_function' in data['neural_net'] and 'beta' in data['neural_net']['activation_function']):
                #     self.beta = data['neural_net']['activation_function']['beta']
                # else:
                #     self.beta = None

                # if('activation_function' in data['neural_net'] and 'type' in data['neural_net']['activation_function']):
                #     self.activationFunctionType = data['neural_net']['activation_function']['type']
                # else:
                #     self.activationFunctionType = None

                #Pedimos las funciones de activacion del encoder, el espacio latente y el decoder
                #Encoder
                if('activation_function' in data['neural_net'] and 'encoder' in data['neural_net']['activation_function'] and 'type' in data['neural_net']['activation_function']['encoder']):
                    self.encoderActivationFunctionType = data['neural_net']['activation_function']['encoder']['type']
                else:
                    self.encoderActivationFunctionType = None

                if('activation_function' in data['neural_net'] and 'encoder' in data['neural_net']['activation_function'] and 'beta' in data['neural_net']['activation_function']['encoder']):
                    self.encoderBeta = data['neural_net']['activation_function']['encoder']['beta']
                else:
                    self.encoderBeta = None

                #Espacio latente
                if('activation_function' in data['neural_net'] and 'latent_space' in data['neural_net']['activation_function'] and 'type' in data['neural_net']['activation_function']['latent_space']):
                    self.latentSpaceActivationFunctionType = data['neural_net']['activation_function']['latent_space']['type']
                else:
                    self.latentSpaceActivationFunctionType = None

                if('activation_function' in data['neural_net'] and 'encoder' in data['neural_net']['activation_function'] and 'beta' in data['neural_net']['activation_function']['latent_space']):
                    self.latentSpaceBeta = data['neural_net']['activation_function']['latent_space']['beta']
                else:
                    self.latentSpaceBeta = None


                #Decoder
                if('activation_function' in data['neural_net'] and 'decoder' in data['neural_net']['activation_function'] and 'type' in data['neural_net']['activation_function']['decoder']):
                    self.decoderActivationFunctionType = data['neural_net']['activation_function']['decoder']['type']
                else:
                    self.decoderActivationFunctionType = None

                if('activation_function' in data['neural_net'] and 'encoder' in data['neural_net']['activation_function'] and 'beta' in data['neural_net']['activation_function']['decoder']):
                    self.decoderBeta = data['neural_net']['activation_function']['decoder']['beta']
                else:
                    self.decoderBeta = None
                
                
                ##Pidiendo las propiedades de backtracking
                #learningRate
                if('learning_rate' in data['backtracking']):
                    self.learningRate = data['backtracking']['learning_rate']
                else:
                    self.learningRate = None

                ##Pidiendo las propiedades del problema en general
                #maxEpochs
                if('max_epochs' in data):
                    self.maxEpochs = data['max_epochs']
                else:
                    self.maxEpochs = None
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
                ##font
                if('font' in data):
                    self.font = data['font']
                else:
                    self.font = None
                ##noiseProbability
                if('noise_probability' in data):
                    self.noiseProbability = data['noise_probability']
                else:
                    self.noiseProbability = None
                ##noiseRange
                if('noise_range' in data):
                    self.noiseRange = data['noise_range']
                else:
                    self.noiseRange = None
                
            #Finalmente, le asignamos una propiedad que indique si las anteriores leidas son validas o no
            self.isValid = self.validateConfigurationProperties()
        


    def __str__(self):
        return f"\t-Architecture : {self.architecture}\n\t\t-Activation function :{self.activationFunctionType}\n\t\t-Beta : {self.beta}\n\t\t-Learning rate : {self.learningRate} \n\t\t-Max epochs : {self.maxEpochs}\n\t\t-Error bound : 1e^{self.maxToleranceExponent}"

    def __repr__(self) -> str:
        return self.__str__()

    def getProperties(self):
        #Obtenemos las funciones de activacion del encoder, espacio latente y el decoder
        #Encoder
        encoderActivationFunctionClass = self.getActivationFunctionClass(self.encoderActivationFunctionType.strip().upper())
        encoderActivationFunction = encoderActivationFunctionClass.getType(self.encoderBeta)
        #Espacio latente 
        latentSpaceActivationFunctionClass = self.getActivationFunctionClass(self.latentSpaceActivationFunctionType.strip().upper())
        latentSpaceActivationFunction = latentSpaceActivationFunctionClass.getType(self.latentSpaceBeta)
        #Decoder
        decoderActivationFunctionClass = self.getActivationFunctionClass(self.decoderActivationFunctionType.strip().upper())
        decoderActivationFunction = decoderActivationFunctionClass.getType(self.decoderBeta)
        font = self.font.strip().upper()
        return (self.architecture,encoderActivationFunction,latentSpaceActivationFunction,decoderActivationFunction,self.encoderBeta,self.latentSpaceBeta,self.decoderBeta,self.learningRate,self.maxEpochs,self.maxToleranceExponent,self.randomSeed,font,self.noiseProbability,self.noiseRange)

    def validateConfigurationProperties(self):
        return self.__validateNeuralNetProperties() and self.__validateBacktrackingProperties() and self.__validateGeneralProperties()

    def __validateNeuralNetProperties(self):
        return self.__validateArchitecture() and self.__validateActivationFunctionsType() and self.__validateBetas()

    def __validateBacktrackingProperties(self):
        return self.__validateLearningRate()

    def __validateGeneralProperties(self):
        return self.__validateMaxEpochs() and self.__validateMaxToleranceExponent() and self.__validateRandomSeed() and self.__validateFont() and self.__validateNoiseProbability() and self.__validateNoiseRange()

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
        isValid = isinstance(self.architecture,list) and len(self.architecture)>=3 and all((isinstance(x, int) and x>0) for x in self.architecture) and len(self.architecture)%2==1 and self.architecture==list(reversed(self.architecture))
        if(not isValid):
            print("Illegal architecture : Should be an array of integer positive numbers, with odd length and reversed architecture must be equal to original")
        return isValid

    def __validateActivationFunctionsType(self):
        isValid = self.encoderActivationFunctionType is not None and isinstance(self.encoderActivationFunctionType,str) and self.latentSpaceActivationFunctionType is not None and isinstance(self.latentSpaceActivationFunctionType,str) and self.decoderActivationFunctionType is not None and isinstance(self.decoderActivationFunctionType,str)
        if(not isValid):
            print('It is required to determine a "activationFunctionType" in a form of a string.')
            return isValid
        encoderActivationFunctionClass=self.getActivationFunctionClass(self.encoderActivationFunctionType.strip().upper())
        latentSpaceActivationFunctionClass=self.getActivationFunctionClass(self.latentSpaceActivationFunctionType.strip().upper())
        decoderActivationFunctionClass=self.getActivationFunctionClass(self.decoderActivationFunctionType.strip().upper())
        if(encoderActivationFunctionClass is None or latentSpaceActivationFunctionClass is None or decoderActivationFunctionClass is None):
            print("Illegal activation function used")
            return False
        return isValid

    def __validateBetas(self):
        if(self.encoderBeta is None and self.latentSpaceBeta is None and self.decoderBeta is None):
            self.encoderBeta = self.DEFAULT_BETA
            self.latentSpaceBeta = self.DEFAULT_BETA
            self.decoderBeta = self.DEFAULT_BETA
            return True
        else:
            if(self.encoderBeta is None):
                self.encoderBeta = self.DEFAULT_BETA
            if(self.latentSpaceBeta is None):
                self.latentSpaceBeta = self.DEFAULT_BETA
            if(self.decoderBeta is None):
                self.decoderBeta = self.DEFAULT_BETA
            isValid = (isinstance(self.encoderBeta,float) and self.encoderBeta > 0 and self.encoderBeta<=1) or (isinstance(self.encoderBeta,int) and self.encoderBeta==1) and (isinstance(self.latentSpaceBeta,float) and self.latentSpaceBeta > 0 and self.latentSpaceBeta<=1) or (isinstance(self.latentSpaceBeta,int) and self.latentSpaceBeta==1) and (isinstance(self.decoderBeta,float) and self.decoderBeta > 0 and self.decoderBeta<=1) or (isinstance(self.decoderBeta,int) and self.decoderBeta==1)
            if(not isValid):
                print("Illegal beta : Should be a positive decimal number between 0 and 1 (zero excluded, one included)")
            return isValid

    def __validateMaxEpochs(self):
        if(self.maxEpochs is None):
            print(" 'max_epochs' is a required parameter")
            return False
        isValid = isinstance(self.maxEpochs,int) and self.maxEpochs > 0
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

    def __validateFont(self):
        if(self.font is None):
            print(" 'font' is a required parameter")
            return False
        isValid = self.font.strip().upper() in possibleFonts
        if(not isValid):
            print("Illegal font : Font do not exists")
        return isValid

    def __validateNoiseProbability(self):
        if(self.noiseProbability is None):
            print(" 'noise_probability' is a required parameter")
            return False
        isValid = (isinstance(self.noiseProbability,float) and self.noiseProbability > 0 and self.noiseProbability<=1) or (isinstance(self.noiseProbability,int) and self.noiseProbability==1)
        if(not isValid):
            print("Illegal noise probability : Should be a positive decimal number between 0 and 1")
        return isValid

    def __validateNoiseRange(self):
        if(self.noiseRange is None):
            print(" 'noise_range' is a required parameter")
            return False
        isValid = (isinstance(self.noiseRange,float) or isinstance(self.noiseRange,int)) and self.noiseRange>0
        if(not isValid):
            print("Illegal noise range : Should be a positive number")
        return isValid

    @staticmethod
    def getActivationFunctionClass(type):
        return possibleActivationFunctionTypes.get(type)


