def eliteSelection(selectionIndividuals,targetPoblationSize):
    
    #Ordenamos la poblacion por mayor fitness, y retornamos los primeros "targetPoblationSize"
    return sorted(selectionIndividuals,key=lambda x: x.fitness)[0:targetPoblationSize]

    

