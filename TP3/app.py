import argparse,os

from bs4 import ResultSet
from helpers.readSetFiles import readSetFiles,validateParameters
from graph import plotEpochsError,plotGraphEj1
from helpers.configHelper import ConfigHelper
from neuralNetworkManager import NeuralNetworkManager
from output import Output
import numpy as np
import random    

def main():
    print("proyectazo de SIA-TP3")
   
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
        (trainingSet,resultSet) = readSetFiles(trainSetFile , outputFile)
        configHelper = ConfigHelper(configPath)
        if(configHelper.isValid):

            ##Setear el seed para todos los random que se utilicen en el algoritmo
            random.seed(configHelper.randomSeed)
            np.random.seed(configHelper.randomSeed)

            (architecture,activationFunction,beta,learningRate,maxEpochs,maxToleranceExponent,randomSeed) = configHelper.getProperties()

            fileParametersValid = validateParameters(trainingSet,resultSet,(architecture[0],architecture[-1]))
            if(fileParametersValid):



                neuralNetworkManager = NeuralNetworkManager(architecture,activationFunction,learningRate,maxEpochs,maxToleranceExponent)
                (epochs,executionTime,exception) = neuralNetworkManager.start(trainingSet,resultSet)
                 ##Imprimir la salida correspondiente
                print("FINISH-------------------------------------------------------------------------------------------")
                output = Output(configHelper,epochs[-1].error,epochs[-1].epochNumber,executionTime)
                output.printOutput()
                #plot
                plotEpochsError(epochs)


    else:
        print("Training set and results set files\'s pathnames are required")

def normalize(Y,lowerBoundary,upperBoundary): 
    maxElem = max([max(elem) for elem in Y])
    minElem = min([min(elem) for elem in Y])
    fix =lambda elem: (upperBoundary-lowerBoundary)*(elem - minElem)/(maxElem-minElem) + lowerBoundary
    fixnt= lambda elem: minElem + ((elem -lowerBoundary)* (maxElem-minElem))/(upperBoundary-lowerBoundary)
    return ([list(map(fix,sublist)) for sublist in Y],fixnt)



if __name__ == "__main__":
    main()