
import argparse
import time
import random
import numpy as np
from output import Output
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

        ##Setear el seed para todos los random que se utilicen en el algoritmo
        random.seed(configHelper.randomSeed)
        np.random.seed(configHelper.randomSeed)

        ##Empezar el populationManager con los datos del algoritmo genetico y del problema
        populationManager = PopulationManager(configHelper.populationSize,configHelper.maxRangeGen,configHelper.replacement,crossMethod,selectionMethod,mutationMethod,Fitness(configHelper.epsilon.reactives,configHelper.c),finishCondition)
        (bestIndividual,populations,executionTime)=populationManager.start()
        ##Imprimir la salida correspondiente
        print("FINISH-------------------------------------------------------------------------------------------")
        output = Output(configHelper, populations,bestIndividual,executionTime)
        output.printOutput()
        #plot
        plotGenerationsFitness(populations)


if __name__ == "__main__":
    main()