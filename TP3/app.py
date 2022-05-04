import argparse,os
from helpers.readSetFiles import readSetFiles,validateParameters
from graph import plotEpochsError
from helpers.configHelper import ConfigHelper
from helpers.activationFunctionHelper import ActivationFunctionHelper
from neuralNetworkManager import NeuralNetworkManager
from output import Output
import numpy as np
import random    

def main():
    print("proyectazo de SIA-TP3")
   
    np.random.seed(10)
    random.seed(10)

    configPath="./config/config.json"
    trainSetFile = None
    outputFile = None
    resultsFolderName = "results"
    graphsFolderName = "graphs"
    graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c','--configPath',dest='configPath')
        parser.add_argument('-t' '--trainSetFile' , dest='trainSetFile')
        parser.add_argument('-o' ,'--outputFile' , dest='outputFile')
        args = parser.parse_args()
        if(args.configPath is not None):
            configPath=args.configPath
            
        if(args.trainSetFile is not None):
            trainSetFile=args.trainSetFile
        if(args.outputFile is not None):
            outputFile = args.outputFile
    except Exception as e:
        print("Error in command line arguments")
        print(e)

    ##Crear la carpeta de resultados con la subcarpeta de graficos y estadisticas en caso de que no existan
    if(not os.path.exists(graphsPath)):
        os.makedirs(graphsPath)

    ##Checkeamos que nos hayan pasado los paths correspondientes al archivo de entrenamiento y el de salida
    if(trainSetFile is not None and outputFile is not None):
        ##Crear los helpers
        # print(trainSetFile)
        # print(outputFile)
        (trainingSet,resultSet) = readSetFiles(trainSetFile , outputFile)
        configHelper = ConfigHelper(configPath)
        activationFunctionHelper = ActivationFunctionHelper()
        # print(trainingSet)
        # print(resultSet)
        if(configHelper.validateConfigurationProperties()):

            fileParametersValid = validateParameters(trainingSet,resultSet,(configHelper.architecture[0],configHelper.architecture[-1]))
            if(fileParametersValid):
   
                # trainingSet=[[-1,1],[1,-1],[-1,-1],[1,1]]
                # resultsSet=[[1,1],[1,1],[-1,-1],[1,1]]
                #resultsSet=[1,1,-1,-1]

                #Normalizamos el conjunto de salida
                resultSet=normalize(resultSet,0.05,0.98)
                trainingSet=normalize(trainingSet,-0.98,0.98)
                
                activationFunction = activationFunctionHelper.getActivationFunctionType(configHelper.activationFunctionType)

                # print('architecture : '+str(configHelper.architecture))
                # print('activation function : '+activationFunction.name)
                # print('learning rate : '+str(configHelper.learningRate))
                # print('max iterations : '+str(configHelper.maxIterations))

                neuralNetworkManager = NeuralNetworkManager(configHelper.architecture,activationFunction,configHelper.learningRate,configHelper.maxIterations,configHelper.maxToleranceExponent)
                (epochs,executionTime) = neuralNetworkManager.start(trainingSet,resultSet)
                 ##Imprimir la salida correspondiente
                print("FINISH-------------------------------------------------------------------------------------------")
                output = Output(configHelper,epochs[-1].error,epochs[-1].iterationNumber,executionTime)
                output.printOutput()
                #plot
                plotEpochsError(epochs)

    else:
        print("Training set and results set files\'s pathnames are required")

def normalize(Y,lowerBoundary,upperBoundary):
    print("----------------------------------------------------\n",Y)
    #for elem in Y:
        #print(max[elem)
    maxElem = max([max(elem) for elem in Y])
    minElem = min([min(elem) for elem in Y])
    fix =lambda elem: (upperBoundary-lowerBoundary)*(elem - minElem)/(maxElem-minElem) + lowerBoundary
    #fixSublist = lambda sublist: 
    return [list(map(fix,sublist)) for sublist in Y]



if __name__ == "__main__":
    main()