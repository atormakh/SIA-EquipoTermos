import matplotlib
from mutation import Mutation
from fitness import Fitness
from poblationManager import PoblationManager
from selectionMethods.eliteSelection import eliteSelection
from crossingMethods.simpleCross import simpleCross
import pandas as pd
import matplotlib.pyplot as plt



def main():
    print("proyectazo de SIA-TP2")
    epsilon = [[4.4793,-4.0765,-4.0765],[-4.1793,-4.9218,1.7664],[-3.9429,-0.7689,4.8830]]
    c = [0,1,1]
    # Parsear parametros de entrada
    maxGenerationSize=100
    poblationSize=100
    crossMethod= simpleCross
    selectionMethod=eliteSelection
    mutation=Mutation(0.05,3)
    poblationManager = PoblationManager(maxGenerationSize,poblationSize,crossMethod,selectionMethod,mutation,Fitness(epsilon,c))
    (bestIndividual,poblations)=poblationManager.start()

    print("FINISH-------------------------------------------------------------------------------------------")
    print("Best individual=="+ str(bestIndividual))
    #pandas
    data = {
        'Generation':[],
        'Fitness':[]
    }
    for poblation in poblations:
        data["Generation"].append(poblation.generation)
        data["Fitness"].append(poblation.maxFitnessIndividual.fitness)

    table = pd.DataFrame(data)
    print(table.head())
    table.plot(x="Generation")
    plt.show()





if __name__ == "__main__":
    main()