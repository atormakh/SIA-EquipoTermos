
import argparse
import random
import numpy as np
import os
from selectionMethods.truncatedSelection import TruncatedSelection
from selectionMethods.tournamentSelection import TournamentSelection
from output import Output
from graph import plotGenerationsFitness,plotVariablesPlotter
from fitness import Fitness
from populationManager import PopulationManager
from helpers.configHelper import ConfigHelper
from helpers.geneticHelper import GeneticHelper

def main():
    print("proyectazo de SIA-TP2")

    configPath="./config/config.json"
    resultsFolderName = "results"
    graphsFolderName = "graphs"
    statsFolderName = "stats"
    graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
    statsPath = f"./{resultsFolderName}/{statsFolderName}"

    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c','--configPath',dest='configPath')
        args = parser.parse_args()
        if(args.configPath is not None):
            configPath=args.configPath
    except Exception as e:
        print("Error in command line arguments")
        print(e)

    ##Crear la carpeta de resultados con la subcarpeta de graficos y estadisticas en caso de que no existan
    if(not os.path.exists(graphsPath)):
        os.makedirs(graphsPath)

    if(not os.path.exists(statsPath)):
        os.makedirs(statsPath)

    #Eliminar los graficos viejos
    for f in os.listdir(graphsPath):
        os.remove(os.path.join(graphsPath, f))

    ##Crear el configHelper principal
    configHelper1 = ConfigHelper(configPath)
    
    configHelpers = [configHelper1]
    
    if(configHelper1.isMulti):
        configHelpers = configHelper1.multi

    populationsHistory =[]

    variableRange = []
    repetitions=[]
    step=(configHelpers[0].populationSize/5)-4
    i=5
    while i<=configHelpers[0].populationSize:
        variableRange.append(i)
        i+=int(step)
        repetitions.append(i%4)
    print(f"populationSize={configHelpers[0].populationSize}")
    print(variableRange)



    if(configHelper1.allValid or True):

        for u in variableRange:
            repetitionsAcum=0
            for r in repetitions:
                #Crear el geneticHelper
                geneticHelper = GeneticHelper()
                configHelper = configHelpers[0]
                if(configHelper.validateConfigurationProperties()):

                    ##Pedir el metodo de cruza, mutacion, seleccion y condicion de corte utilizados
                    crossMethod = geneticHelper.getCrossMethod(configHelper.crossData)
                    mutationMethod =  geneticHelper.getMutationMethod(configHelper.mutationData)
                    selectionMethod = TruncatedSelection(u) #geneticHelper.getSelectionMethod(configHelper.selectionData)
                    finishCondition = geneticHelper.getFinishCondition(configHelper.finishConditionData)

                    ##Setear el seed para todos los random que se utilicen en el algoritmo
                    random.seed(configHelper.randomSeed+r)
                    np.random.seed(configHelper.randomSeed)

                    ##Inicializar la funcion de fitness a utilizar
                    fitness = Fitness(configHelper.epsilon.reactives,configHelper.c)

                    ##Empezar el populationManager con los datos del algoritmo genetico y del problema
                    populationManager = PopulationManager(configHelper.populationSize,configHelper.maxRangeGen,configHelper.replacement,crossMethod,selectionMethod,mutationMethod,fitness,finishCondition)
                    (bestIndividual,populations,executionTime)=populationManager.start()
                    ##Imprimir la salida correspondiente
                    print("FINISH-------------------------------------------------------------------------------------------")
                    output = Output(configHelper, populations,bestIndividual,executionTime,fitness)
                    output.printOutput()
                    output.writeToFile()
                    
                    #plot
                    #plotGenerationsFitness(populations,configHelper1.allCategory,configHelper.getAllCategoryData(configHelper1.allCategory))
                    repetitionsAcum+=len(populations)
            populationsHistory.append(repetitionsAcum/len(repetitions))
    else:
        print('Illegal ALL option')

    plotVariablesPlotter(populationsHistory,variableRange)


if __name__ == "__main__":
    main()