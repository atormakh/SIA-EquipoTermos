import random
from individual import Individual

def multipleCross(i1,i2,indexCount):
    MAX_INDIVIDUAL_SIZE = 11
    isIndexesSameLengthAsIndividual = False
    
    #Primero, creamos los genes de los descendientes vacios y un array donde se guardaran los indices a establecer
    genes1 = []
    genes2 = []
    indexes = []

    #Luego, generamos los indices. En caso de que el indexCount sea igual al tamano del cromosoma del individuo, se copian todos sus indices. Caso contrario, se generan random
    if(indexCount == MAX_INDIVIDUAL_SIZE):
        isIndexesSameLengthAsIndividual = True
        for i in range(0,MAX_INDIVIDUAL_SIZE):
            indexes.append(i)
    else:
        while(len(indexes)!=indexCount):
            possibleIndex = random.randint(0,MAX_INDIVIDUAL_SIZE-1)
            #En caso de no haber sido elegido, se agrega al array de indices
            if(possibleIndex not in indexes):
                indexes.append(possibleIndex)
    
        #Una vez hecho esto, se ordena dicho array para que los indices queden en orden
        indexes.sort()

    #Luego, recorremos el array de indices, y alternadamente intercambiamos los genes de los individuos o no para los descendientes
    for i in range(0,len(indexes)):
        #Para indices de posicion par, no intercambiamos. Caso contrario, si
        if(i % 2 == 0):
            #Si es el primer indice, debemos arrancar desde el principio, sino desde el indice anterior
            if(i == 0):
                genes1.extend(i1.genes[0:indexes[i]+1])
                genes2.extend(i2.genes[0:indexes[i]+1])
            else:
               genes1.extend(i1.genes[indexes[i-1]+1:indexes[i]+1])
               genes2.extend(i2.genes[indexes[i-1]+1:indexes[i]+1])
        else:
            genes1.extend(i2.genes[indexes[i-1]+1:indexes[i]+1])
            genes2.extend(i1.genes[indexes[i-1]+1:indexes[i]+1])
    
    #En caso de que el array de indices no tenga la misma longitud que el cromosoma del individuo, debemos completar los genes de los descendientes segun corresponda
    if(not isIndexesSameLengthAsIndividual):
        lastIndex = indexes[i]
        #Si en el ultimo indice intercambio, aca no tiene que hacerlo, y viceversa
        if(i % 2 == 0):
            genes1.extend(i2.genes[lastIndex+1:MAX_INDIVIDUAL_SIZE])
            genes2.extend(i1.genes[lastIndex+1:MAX_INDIVIDUAL_SIZE])
        else:
            genes1.extend(i1.genes[lastIndex+1:MAX_INDIVIDUAL_SIZE])
            genes2.extend(i2.genes[lastIndex+1:MAX_INDIVIDUAL_SIZE])

    #Finalmente, creamos y retornamos los individuos con los nuevos genes
    newIndividual1 = Individual(genes1)
    newIndividual2=Individual(genes2)
    return [newIndividual1,newIndividual2]


