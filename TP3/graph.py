import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
import numpy as np

def plotMetricAgainstVariable(metricArray,metricTitle,variableArray,variableTitle):
    plt.figure(f"{metricTitle} vs {variableTitle}")
    data = {
        'Metric':[],
        'Variable':[],
    }
    for i in range(0,len(variableArray)):
        
        data["Metric"].append(metricArray[i])
        data["Variable"].append(variableArray[i])
        

    table = pd.DataFrame(data)
    table.plot(x="Variable")
    destinationPath = "./results/graphs/"
    fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    #plt.savefig(f"{destinationPath}{fileName}")
    plt.xlabel(f"{variableTitle}")
    plt.ylabel(f"{metricTitle}")
    plt.show()


def plotMetricsAgainstVariable(metricsDict,variableArray,variableTitle):
    
    for metric,values in metricsDict.items():
        plt.figure(f"{metric} vs {variableTitle}")
        data = {
            'Metric':[],
            'Variable':[],
        }
        # for net in epochs:
            
        #     data["Epoch"].append(net.iterationNumber)
        #     data["Error"].append(net.error)
        for i in range(0,len(variableArray)):
            data["Metric"].append(values[i])
            data["Variable"].append(variableArray[i])
    
        table = pd.DataFrame(data)
        table.plot(x="Variable")
        destinationPath = "./results/graphs/"
        fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    #plt.savefig(f"{destinationPath}{fileName}")
        plt.title(f"{metric} vs {variableTitle}")
        plt.xlabel(f"{variableTitle}")
        plt.ylabel(f"{metric}")
        plt.show()


def plotEpochsError(epochs,title=None,denormalizeFn=None,testingSetErrors=None):
    plt.figure("Error vs Epoch")
    data = {
        'Epoch':[],
        'Error':[],
    }
    for net in epochs:
        
        data["Epoch"].append(net.iterationNumber)
        data["Error"].append(net.error)

    if(denormalizeFn is not None):
        data["RealError"]=[]
        for net in epochs:
            data["RealError"].append(denormalizeFn(net.error))
    if(testingSetErrors is not None):
        data["TestingSetError"]=[]
        for err in testingSetErrors:
            data["TestingSetError"].append(err)
        

    table = pd.DataFrame(data)
    plt.ylabel("Error")
    plt.xlabel("Epoch")
    plt.plot(data["Epoch"],data["Error"])
    if title is not None:
        plt.title(title)
    
    if testingSetErrors is not None:
        plt.plot(data["Epoch"],data["TestingSetError"],c="orange")
    if denormalizeFn is not None:
        plt.plot(data["Epoch"],data["RealError"])
        if title is not None:
            plt.title(f"{title} Real Error ")
    plt.show()
def plotErrorAgainstKGraph(errors,ks):
    data = {
        'K':[],
        'Error':[],
    }
    data["K"] = ks
    data["Error"]=errors
    # for net in epochs:
        
    #     data["Epoch"].append(net.iterationNumber)
    #     data["Error"].append(net.error)
        

    table = pd.DataFrame(data)
    table.plot(x="K")
    destinationPath = "./results/graphs/"
    fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    plt.figure("Error vs K")
    #plt.savefig(f"{destinationPath}{fileName}")
    plt.show()

def plotErrorAgainstTrainingPercentageGraph(errors,trainingPercentages):
    data = {
        'Training percentage':[],
        'Error':[],
    }
    data["Training percentage"] = trainingPercentages
    data["Error"]=errors
    # for net in epochs:
        
    #     data["Epoch"].append(net.iterationNumber)
    #     data["Error"].append(net.error)
        

    table = pd.DataFrame(data)
    table.plot(x="Training percentage")
    destinationPath = "./results/graphs/"
    fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    plt.figure("Error vs Training percentage")
    #plt.savefig(f"{destinationPath}{fileName}")
    plt.show()

def plotGraphEj1(trainingSet,isXOR,epochs):
    plt.figure('Division graph - Ej 1')

    #Primero grafica los puntos
    for tr in range(0,len(trainingSet)):
        trainingArray = trainingSet[tr]
        x = trainingArray[0]
        y = trainingArray[1]
        plt.scatter(x,y,c=__getPointColor(x,y,isXOR))
    #Luego, por cada epoca, grafica el plano de separacion
    for i in range(0,len(epochs)):
        x = np.linspace(-1, 1, 100)
        W = epochs[i].layers[0].W
        plt.plot(x,__functionEj1(W,x),c=__getRandomColor(),label = f"epoch {i}")
    #Finalmente, mostramos el grafico
    # if(not isXOR):
    #     plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def plotGraphEj1Animated(trainingSet,isXOR,epochs,isEj1):

    excercise = 'Ej1'
    if(not isEj1):
        excercise = 'Ej3_1'

    plt.figure(f"Division graph animated - {excercise}")

    # Create variable reference to plot
    f_d, = plt.plot([], [], linewidth=2.5)
    # Add text annotation and create variable reference
    text = plt.text(1, 1, '', ha='right', va='top', fontsize=24)
    
    #Primero grafica los puntos
    for tr in range(0,len(trainingSet)):
        trainingArray = trainingSet[tr]
        x = trainingArray[0]
        y = trainingArray[1]
        plt.scatter(x,y,c=__getPointColor(x,y,isXOR))

    def animate(i):
        x = np.linspace(-1, 1, 100)
        W = epochs[i].layers[0].W
        # x = np.linspace(0, 1, 100)
        # y = fermi(x, 0.5, T[i])
        f_d.set_data(x, __functionEj1(W,x))
        # randomColor = __getRandomColor()
        color = 'green'
        f_d.set_color(color)
        text.set_text(f"epoch {i}")
        text.set_color(color)

    ani = FuncAnimation(fig=plt.gcf(), func=animate, frames=range(len(epochs)), interval=5, repeat=True)
    destinationPath = "./results/graphs/"
    if(not os.path.exists(destinationPath)):
        os.makedirs(destinationPath)
    if(isXOR):
        fileName = f"Animated{excercise}XORGraph.gif"
    else:
        fileName = f"Animated{excercise}ANDGraph.gif"

    # plt.show()
    ani.save(f"{destinationPath}{fileName}", writer='imagemagick', fps=15)
        

def __functionEj1(W,x):
    # print("W in func==",W)
    # w0 = W.item((0,0))
    # w1 = W.item((0,1))
    # w2 = W.item((0,2))
    w0 = W.A[0][0]
    w1 = W.A[0][1]
    w2 = W.A[0][2]
    # print('w0==',w0)
    # print('w1==',w1)
    # print('w2==',w2)

    return (-w1/w2)* x - w0/w2

def __getPointColor(x,y,isXOR=True):
    if(isXOR):
        if(x!=y):
            return 'blue'
        return 'black'
    else:
        if(x*y==-1 or (x==-1 and y==-1)):
            return 'black'
        return 'blue'

def __getRandomColor():
    r = np.random.random()
    g = np.random.random()
    b = np.random.random()
    return (r,g,b)
