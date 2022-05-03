import pandas as pd
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
    print(table.head())
    table.plot(x="Epoch")
    destinationPath = "./results/graphs/"
    fileName = "Graph"
    #if(allCategory is not None):
    #    fileName = f"Graph_{allCategory}_{allCategoryData['method'].lower()}"
    plt.savefig(f"{destinationPath}{fileName}")

def plotPointsEj1(W,trainingSet,i):
    # x = np.array([1,-1])
    x = np.linspace(-1, 1, 100)
    print('x==',x)
    destinationPath = "./results/graphs/"
    fileName = f"Ej1_plot{i}"
    plt.figure(i)
    plt.plot(x,functionEj1(W,x),color='green')
    for tr in range(0,len(trainingSet)):
        trainingArray = trainingSet[tr]
        x = trainingArray[0]
        y = trainingArray[1]
        plt.scatter(x,y,c=getColor(x,y,False))
    plt.savefig(f"{destinationPath}{fileName}")

def functionEj1(W,x):
    w0 = W.A[0][0]
    w1 = W.A[0][1]
    w2 = W.A[0][2]

    return (-w1/w2)* x - w0/w2

def getColor(x,y,isXOR=True):
    if(isXOR):
        if(x!=y):
            return 'blue'
        return 'black'
    else:
        if(x*y==-1 or (x==-1 and y==-1)):
            return 'black'
        return 'blue' 
