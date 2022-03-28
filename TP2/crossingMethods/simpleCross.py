import random

from individual import Individual

def simpleCross(i1,i2,crossIndexCount=None):
    
    #Creamos los genes de los descendientes vacios, y calculamos un indice random
    p = random.randint(0,len(i1.genes))
    genes1=[]
    genes2=[]

    #Dejamos los primeros p genes de cada individuo iguales
    for i in range(0,p):
        genes1.append(i1.genes[i])
        genes2.append(i2.genes[i])

    #El resto de los genes se intercambian entre los individuos
    for i in range(p,len(i1.genes)):
        genes1.append(i2.genes[i])
        genes2.append(i1.genes[i])

    #Finalmente, creamos y retornamos los individuos con los nuevos genes
    newIndividual1 = Individual(genes1)
    newIndividual2=Individual(genes2)
    return [newIndividual1,newIndividual2]