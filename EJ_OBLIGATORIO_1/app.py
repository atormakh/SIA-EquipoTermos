
import argparse
import random
import numpy as np
import os
from output import Output
# from graph import plotGenerationsFitness
from function import Function
from helpers.configHelper import ConfigHelper
from helpers.optimizationHelper import OptimizationHelper
from optimizationManager import OptimizationManager

def main():
    print("Ej obligatorio 1 de SIA")

    configPath="./config/config.json"
    # resultsFolderName = "results"
    # graphsFolderName = "graphs"
    # statsFolderName = "stats"
    # graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
    # statsPath = f"./{resultsFolderName}/{statsFolderName}"

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

    # if(not os.path.exists(statsPath)):
    #     os.makedirs(statsPath)

    # #Eliminar los graficos viejos
    # for f in os.listdir(graphsPath):
    #     os.remove(os.path.join(graphsPath, f))

    ##Crear los helpers
    configHelper = ConfigHelper(configPath)
    optimizationHelper = OptimizationHelper()

    if(configHelper.validateConfigurationProperties()):
        ##Pedir el metodo de optimizacion
        optimizationMethod = optimizationHelper.getOptimizationMethod(configHelper.method)

        ##Setear el seed para todos los random que se utilicen en el algoritmo
        random.seed(configHelper.randomSeed)
        np.random.seed(configHelper.randomSeed)

        ##Inicializar la funcion a utilizar
        function = Function(configHelper.epsilon.reactives,configHelper.c)

        # ##Empezar el optimizationManager con los datos del algoritmo de optimizacion y del problema
        optimizationManager = OptimizationManager(optimizationMethod,configHelper.maxRangeGen,configHelper.maxToleranceExponent,function)
        (bestIndividual,individuals,executionTime)=optimizationManager.start()
        #Imprimir la salida correspondiente
        print("FINISH-------------------------------------------------------------------------------------------")
        output = Output(configHelper, individuals,bestIndividual,executionTime,function)
        output.printOutput()
        # #plot
        # plotGenerationsFitness(populations)


######################################CODIGO CON EL ALL #################################################################################################################

    # ##Crear el configHelper principal
    # configHelper1 = ConfigHelper(configPath)
    
    # configHelpers = [configHelper1]
    # if(configHelper1.isMulti):
    #     configHelpers = configHelper1.multi

    # if(configHelper1.allValid):

    #     for configHelper in configHelpers:

    #         #Crear el geneticHelper
    #         geneticHelper = GeneticHelper()

    #         if(configHelper.validateConfigurationProperties()):

    #             ##Pedir el metodo de cruza, mutacion, seleccion y condicion de corte utilizados
    #             crossMethod = geneticHelper.getCrossMethod(configHelper.crossData)
    #             mutationMethod = geneticHelper.getMutationMethod(configHelper.mutationData)
    #             selectionMethod = geneticHelper.getSelectionMethod(configHelper.selectionData)
    #             finishCondition = geneticHelper.getFinishCondition(configHelper.finishConditionData)

    #             ##Setear el seed para todos los random que se utilicen en el algoritmo
    #             random.seed(configHelper.randomSeed)
    #             np.random.seed(configHelper.randomSeed)

    #             ##Inicializar la funcion de fitness a utilizar
    #             fitness = Fitness(configHelper.epsilon.reactives,configHelper.c)

    #             ##Empezar el populationManager con los datos del algoritmo genetico y del problema
    #             populationManager = PopulationManager(configHelper.populationSize,configHelper.maxRangeGen,configHelper.replacement,crossMethod,selectionMethod,mutationMethod,fitness,finishCondition)
    #             (bestIndividual,populations,executionTime)=populationManager.start()
    #             ##Imprimir la salida correspondiente
    #             print("FINISH-------------------------------------------------------------------------------------------")
    #             output = Output(configHelper, populations,bestIndividual,executionTime,fitness)
    #             output.printOutput()
    #             output.writeToFile()
    #             #plot
    #             plotGenerationsFitness(populations,configHelper1.allCategory,configHelper.getAllCategoryData(configHelper1.allCategory))

    # else:
    #     print('Illegal ALL option')


#############################################################################################################################################################################

if __name__ == "__main__":
    main()