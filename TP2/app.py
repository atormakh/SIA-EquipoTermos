from graph import plotGenerationsFitness, plotGenerationsF
from mutation import Mutation
from fitness import Fitness
from populationManager import PopulationManager
from selectionMethods.eliteSelection import eliteSelection
from crossingMethods.simpleCross import simpleCross




def main():
    print("proyectazo de SIA-TP2")
    epsilon = [[4.4793,-4.0765,-4.0765],[-4.1793,-4.9218,1.7664],[-3.9429,-0.7689,4.8830]]
    c = [0,1,1]
    # Parsear parametros de entrada
    maxGenerationSize=25
    populationSize=10
    crossMethod= simpleCross
    selectionMethod=eliteSelection
    mutation=Mutation(0.05,3)
    fitness=Fitness(epsilon,c)
    populationManager = PopulationManager(maxGenerationSize,populationSize,crossMethod,selectionMethod,mutation,fitness)
    (bestIndividual,populations)=populationManager.start()

    print("FINISH-------------------------------------------------------------------------------------------")
    print("Best individual=="+ str(bestIndividual))
    #plot
    plotGenerationsFitness(populations)
    #plotGenerationsF(populations,epsilon,c,fitness)






if __name__ == "__main__":
    main()