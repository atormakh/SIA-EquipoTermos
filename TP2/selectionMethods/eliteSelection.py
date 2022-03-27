def eliteSelection(selectionIndividuals,targetPopulationSize):
    
    #Ordenamos la poblacion por mayor fitness, y retornamos los primeros "targetPopulationSize"
    return sorted(selectionIndividuals,key=lambda x: x.fitness)[0:targetPopulationSize]

    

