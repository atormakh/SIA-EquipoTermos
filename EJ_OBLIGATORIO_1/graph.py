import matplotlib.pyplot as plt

def plotErrorGraph(methods,errors):
    newColors = ['green','blue','purple','brown','teal']
    plt.bar(methods, errors, color=newColors)
    plt.title('Optimization methods Vs Error', fontsize=14)
    plt.xlabel('Optimization method', fontsize=14)
    plt.ylabel('Error', fontsize=14)
    plt.grid(True)
    destinationPath = "./results/graphs/"
    fileName = "errorGraph"
    plt.savefig(f"{destinationPath}{fileName}")

def plotTimeGraph(methods,times):
    newColors = ['green','blue','purple','brown','teal']
    plt.bar(methods,times, color=newColors)
    plt.title('Optimization methods Vs Execution time', fontsize=14)
    plt.xlabel('Optimization method', fontsize=14)
    plt.ylabel('Execution time(s)', fontsize=14)
    plt.grid(True)
    destinationPath = "./results/graphs/"
    fileName = "timeGraph"
    plt.savefig(f"{destinationPath}{fileName}")