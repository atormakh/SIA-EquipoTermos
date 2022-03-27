import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plotGenerationsFitness(poblations):
    data = {
        'Generation':[],
        'Fitness':[]
    }
    for poblation in poblations:
        data["Generation"].append(poblation.generation)
        data["Fitness"].append(poblation.maxFitnessIndividual.fitness)

    table = pd.DataFrame(data)
    print(table.head())
    table.plot(x="Generation", y="Fitness")
    plt.show()

def plotGenerationsF(poblations,epsilon,c,fitness):    
    colormap="spring"
    poblationsData={'E':[1,2,3],'F':c,'Generation':[-1,-1,-1],'Color':["green","green","green"]}
    cmap= cm.get_cmap(colormap)
    for poblation in poblations:
        individual = poblation.maxFitnessIndividual
        color = cmap(poblation.generation/len(poblations))
        e1=fitness.f(individual,epsilon[0])
        e2=fitness.f(individual,epsilon[1])
        e3=fitness.f(individual,epsilon[2])
        poblationsData['E'].append(1)
        poblationsData['F'].append(e1)
        poblationsData['Generation'].append(poblation.generation)
        poblationsData['Color'].append(color)
        poblationsData['E'].append(2)
        poblationsData['F'].append(e2)
        poblationsData['Generation'].append(poblation.generation)
        poblationsData['Color'].append(color)
        poblationsData['E'].append(3)
        poblationsData['F'].append(e3)
        poblationsData['Generation'].append(poblation.generation)
        poblationsData['Color'].append(color)
    poblationsPoints=pd.DataFrame(poblationsData)
    print(poblationsPoints.head())
    poblationsPoints.plot.scatter(x='E',y="F",color=poblationsPoints["Color"],colormap=colormap,colorbar=True)
    plt.show()