
import argparse
from graph import plotGenerationsFitness
from fitness import Fitness
from populationManager import PopulationManager
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
        ##Pedir el metodo de cruza, mutacion, seleccion y condicion de corte utilizados
        crossMethod = geneticHelper.getCrossMethod(configHelper.crossData)
        mutationMethod = geneticHelper.getMutationMethod(configHelper.mutationData)
        selectionMethod = geneticHelper.getSelectionMethod(configHelper.selectionData)
        finishCondition = geneticHelper.getFinishCondition(configHelper.finishConditionData)

        ##Empezar el populationManager con los datos del algoritmo genetico y del problema
        populationManager = PopulationManager(configHelper.populationSize,configHelper.maxRangeGen,crossMethod,selectionMethod,mutationMethod,Fitness(configHelper.epsilon.reactives,configHelper.c),finishCondition)
        (bestIndividual,populations)=populationManager.start()

        ##Imprimir la salida correspondiente
        print("FINISH-------------------------------------------------------------------------------------------")
        print("Best individual=="+ str(bestIndividual))
        #plot
        plotGenerationsFitness(populations)


if __name__ == "__main__":
    main()