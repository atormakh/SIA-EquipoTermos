import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plotEpochsError(epochs):
    data = {
        'Epoch':[],
        'Error':[],
    }
    for net in epochs:
        
        data["Epoch"].append(net.iterationNumber)
        data["Error"].append(net.error)
        

    table = pd.DataFrame(data)
    table.plot(x="Epoch")
    destinationPath = "./results/graphs/"
    fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    plt.figure(0)
    #plt.savefig(f"{destinationPath}{fileName}")
    plt.show()

def plotGraphEj1(trainingSet,isXOR,epochs):
    plt.figure(0)
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
    if(not isXOR):
        plt.legend()
    plt.show()

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
