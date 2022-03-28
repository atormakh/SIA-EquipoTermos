
import argparse
from graph import plotGenerationsFitness, plotGenerationsF
from mutation import Mutation
from fitness import Fitness
from populationManager import PopulationManager
from selectionMethods.eliteSelection import eliteSelection
from crossingMethods.simpleCross import simpleCross
from helpers.configHelper import ConfigHelper
from helpers.geneticHelper import GeneticHelper

def main():
    print("proyectazo de SIA-TP2")

    configPath="./config/config.json"
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c','--configPath',dest='configPath')
        args = parser.parse_args()
        if(args.configPath is not None):
            configPath=args.configPath
    except Exception as e:
        print("Error in command line arguments")
        print(e)

    ##Crear los helpers
    configHelper = ConfigHelper(configPath)
    geneticHelper = GeneticHelper()

    if(configHelper.validateConfigurationProperties()):
        ##Pedir el metodo de cruza y de seleccion utilizado
        selectionMethod = geneticHelper.getSelectionMethod(configHelper.selectionMethod)
        crossMethod = geneticHelper.getCrossMethod(configHelper.crossMethod)

        ##Empezar el populationManager con los datos del algoritmo genetico y del problema
        populationManager = PopulationManager(configHelper.maxGenerationSize,configHelper.populationSize,crossMethod,selectionMethod,configHelper.mutation,Fitness(configHelper.epsilon.reactives,configHelper.c),configHelper.crossIndexCount)
        (bestIndividual,populations)=populationManager.start()

        ##Imprimir la salida correspondiente
        print("FINISH-------------------------------------------------------------------------------------------")
        print("Best individual=="+ str(bestIndividual))
        #plot
        plotGenerationsFitness(populations)


if __name__ == "__main__":
    main()