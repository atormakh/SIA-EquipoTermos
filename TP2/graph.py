import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plotGenerationsFitness(populations):
    data = {
        'Generation':[],
        'best fitness':[],
        'average fitness':[],
        'worst fitness':[]
    }
    for population in populations:
        
        data["Generation"].append(population.generation)
        data["best fitness"].append(population.maxFitnessIndividual.fitness)
        (avg,worst) = calculateGenerationAverageAndWorstFitness(population.individuals)
        data['average fitness'].append(avg)
        data['worst fitness'].append(worst)
    table = pd.DataFrame(data)
    print(table.head())
    table.plot(x="Generation")
    plt.show()

def calculateGenerationAverageAndWorstFitness(population):
    fitnessSum=0
    worstFitness=population[0].fitness
    for individual in population:
        fitnessSum+=individual.fitness
        if individual.fitness < worstFitness:
            worstFitness=individual.fitness
    return (fitnessSum/len(population),worstFitness)

def plotGenerationsF(populations,epsilon,c,fitness):    
    colormap="spring"
    populationsData={'E':[1,2,3],'F':c,'Generation':[-1,-1,-1],'Color':["green","green","green"]}
    cmap= cm.get_cmap(colormap)
    for population in populations:
        individual = population.maxFitnessIndividual
        color = cmap(population.generation/len(populations))
        e1=fitness.f(individual,epsilon[0])
        e2=fitness.f(individual,epsilon[1])
        e3=fitness.f(individual,epsilon[2])
        populationsData['E'].append(1)
        populationsData['F'].append(e1)
        populationsData['Generation'].append(population.generation)
        populationsData['Color'].append(color)
        populationsData['E'].append(2)
        populationsData['F'].append(e2)
        populationsData['Generation'].append(population.generation)
        populationsData['Color'].append(color)
        populationsData['E'].append(3)
        populationsData['F'].append(e3)
        populationsData['Generation'].append(population.generation)
        populationsData['Color'].append(color)
    populationsPoints=pd.DataFrame(populationsData)
    print(populationsPoints.head())
    populationsPoints.plot.scatter(x='E',y="F",color=populationsPoints["Color"],colormap=colormap,colorbar=True)
    plt.show()