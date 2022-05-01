import argparse,os
from graph import plotEpochsError
from helpers.configHelper import ConfigHelper
from helpers.activationFunctionHelper import ActivationFunctionHelper
from helpers.parameterHelper import ParameterHelper
from neuralNetworkManager import NeuralNetworkManager
import sys
    
def main():
    print("proyectazo de SIA-TP3")
   
 
    configPath="./config/config.json"
    trainSetFile = 't'
    outputFile = 'o'
    # resultsFolderName = "results"
    # graphsFolderName = "graphs"
    # graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
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

    # ##Crear la carpeta de resultados con la subcarpeta de graficos y estadisticas en caso de que no existan
    # if(not os.path.exists(graphsPath)):
    #     os.makedirs(graphsPath)

    ##Crear los helpers
    print(trainSetFile)
    print(outputFile)
    paramHelper = ParameterHelper(trainSetFile , outputFile)
    configHelper = ConfigHelper(configPath)
    activationFunctionHelper = ActivationFunctionHelper()
    train = paramHelper.readEntrenamineto()
    out = paramHelper.readSalida()
    print(train)
    print(out)
    out=normalize(out,-1,1)
    print("IGOL CRACK")
    print(out)
    if(configHelper.validateConfigurationProperties()):

        trainingSet=[[-1,1],[1,-1],[-1,-1],[1,1]]
        resultsSet=[[1,1],[1,1],[-1,-1],[-1,-1]]
        #resultsSet=[1,1,-1,-1]
        
        activationFunction = activationFunctionHelper.getActivationFunctionType(configHelper.activationFunctionType)

        print('architecture : '+str(configHelper.architecture))
        print('activation function : '+activationFunction.name)
        print('learning rate : '+str(configHelper.learningRate))
        print('max iterations : '+str(configHelper.maxIterations))

        neuralNetworkManager = NeuralNetworkManager(configHelper.architecture,activationFunction,configHelper.learningRate,configHelper.maxIterations,configHelper.maxToleranceExponent)
        (epochs) = neuralNetworkManager.start(train,out)
        plotEpochsError(epochs)

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