from mutation import Mutation
from fitness import Fitness
from poblationManager import PoblationManager
from selectionMethods.eliteSelection import eliteSelection
from crossingMethods.simpleCross import simpleCross



def main():
    print("proyectazo de SIA-TP2")
    epsilon = [[4.4793,-4.0765,-4.0765],[-4.1793,-4.9218,1.7664],[-3.9429,-0.7689,4.8830]]
    c = [0,1,1]
    # Parsear parametros de entrada
    maxGenerationSize=1000
    poblationSize=10
    crossMethod= simpleCross
    selectionMethod=eliteSelection
    mutation=Mutation(0.20,3)
    poblationManager = PoblationManager(maxGenerationSize,poblationSize,crossMethod,selectionMethod,mutation,Fitness(epsilon,c))
    bestIndividual=poblationManager.start()

    print("FINISH-------------------------------------------------------------------------------------------")
    print("Best individual=="+ str(bestIndividual))


if __name__ == "__main__":
    main()