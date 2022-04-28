import argparse,os
from helpers.configHelper import ConfigHelper
from helpers.activationFunctionHelper import ActivationFunctionHelper

from neuralNetworkManager import NeuralNetworkManager

def main():
    print("proyectazo de SIA-TP3")

    configPath="./config/config.json"
    # resultsFolderName = "results"
    # graphsFolderName = "graphs"
    # graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c','--configPath',dest='configPath')
        args = parser.parse_args()
        if(args.configPath is not None):
            configPath=args.configPath
    except Exception as e:
        print("Error in command line arguments")
        print(e)

    # ##Crear la carpeta de resultados con la subcarpeta de graficos y estadisticas en caso de que no existan
    # if(not os.path.exists(graphsPath)):
    #     os.makedirs(graphsPath)

    ##Crear los helpers
    configHelper = ConfigHelper(configPath)
    activationFunctionHelper = ActivationFunctionHelper()

    if(configHelper.validateConfigurationProperties()):

        trainingSet=[[-1,1],[1,-1],[-1,-1],[1,1]]
        resultsSet=[1,1,-1,-1]

        activationFunction = activationFunctionHelper.getActivationFunctionType(configHelper.activationFunctionType)

        print('architecture : '+str(configHelper.architecture))
        print('activation function : '+activationFunction.name)
        print('learning rate : '+str(configHelper.learningRate))
        print('max iterations : '+str(configHelper.maxIterations))

        neuralNetworkManager = NeuralNetworkManager(configHelper.architecture,activationFunction,configHelper.learningRate,configHelper.maxIterations,configHelper.maxToleranceExponent)
        (neuralNetHistory) = neuralNetworkManager.start(trainingSet,resultsSet)

if __name__ == "__main__":
    main()