import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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