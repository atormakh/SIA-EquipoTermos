import argparse
import random
import numpy as np
import os
from output import Output
from graph import plotErrorGraph,plotTimeGraph
from function import Function
from helpers.configHelper import ConfigHelper
from helpers.optimizationHelper import OptimizationHelper
from optimizationManager import OptimizationManager

def main():
    print("Ej obligatorio 1 de SIA")

    configPath="./config/config.json"
    resultsFolderName = "results"
    graphsFolderName = "graphs"
    graphsPath = f"./{resultsFolderName}/{graphsFolderName}"
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

    ##Crear los helpers
    configHelper = ConfigHelper(configPath)
    optimizationHelper = OptimizationHelper()

    makeGraphs = False
    times = []
    errors = []

    if(configHelper.validateConfigurationProperties()):

        ##Pedir el metodo de optimizacion
        optimizationMethodArray = [configHelper.method]
        if(configHelper.optimizationMethods is not None):
            optimizationMethodArray = configHelper.optimizationMethods
            makeGraphs=True
            #Eliminar los graficos viejos
            for f in os.listdir(graphsPath):
                os.remove(os.path.join(graphsPath, f))

        for optMethod in optimizationMethodArray:
            
            optimizationMethod = optimizationHelper.getOptimizationMethod(optMethod)
            configHelper.setCurrentOptimizationMethod(optMethod)
            ##Setear el seed para todos los random que se utilicen en el algoritmo
            random.seed(configHelper.randomSeed)
            np.random.seed(configHelper.randomSeed)

            ##Inicializar la funcion a utilizar
            function = Function(configHelper.epsilon.reactives,configHelper.c)

            ##Empezar el optimizationManager con los datos del algoritmo de optimizacion y del problema
            optimizationManager = OptimizationManager(optimizationMethod,configHelper.maxRangeGen,function)
            (bestIndividual,error,executionTime)=optimizationManager.start()
            
            #Agregamos los errores y los tiempos de ejecucion a los arrays correspondientes a los graficos (en caso de utilizar el ALL)
            errors.append(error)
            times.append(executionTime)

            #Imprimir la salida correspondiente
            print("FINISH-------------------------------------------------------------------------------------------")
            output = Output(configHelper,bestIndividual,executionTime,function)
            output.printOutput()

        ##En caso de que se haya ejecutado el ALL, se generan los graficos
        if(makeGraphs):
            #plot
            plotErrorGraph(optimizationMethodArray,errors)
            plotTimeGraph(optimizationMethodArray,times)

if __name__ == "__main__":
    main()