import random
import math

from individual import Individual


def uniformCross(i1,i2,crossIndexCount=None):

    #Creamos los genes de los descendientes vacios
    genes1 = []
    genes2 = []

    #Recorremos gen por gen de cada individuo
    for i in range(0,len(i1.genes)):
        #Generamos una probabilidad random
        p = random.random()
        #Si p <= 0.5, el i-esimo gen de i1 sera el i-esimo gen del descendiente 2 y viceversa. Caso contrario, el i-esimo gen de i1 sera el i-esimo gen del descendiente 1 y viceversa
        if(p<0.5 or math.isclose(p,0.5)):
            genes1.append(i2.genes[i])
            genes2.append(i1.genes[i])
        else:
            genes1.append(i1.genes[i])
            genes2.append(i2.genes[i])
    
    #Finalmente, creamos y retornamos los individuos con los nuevos genes
    newIndividual1 = Individual(genes1)
    newIndividual2=Individual(genes2)
    return [newIndividual1,newIndividual2]