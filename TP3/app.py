import argparse,os
from platform import architecture

from neuralNetworkManager import NeuralNetworkManager

def main():
    print("proyectazo de SIA-TP3")
    trainingSet=[[-1,1],[1,-1],[-1,-1],[1,1]]
    resultsSet=[1,1,-1,-1]

    architecture=[2,5,4,1]
    activationFunction='sigmoid'
    learningRate=0.1
    max_iterations=200

    neuralNetworkManager = NeuralNetworkManager(architecture,activationFunction,learningRate,max_iterations)
    (neuralNetHistory) = neuralNetworkManager.start(trainingSet,resultsSet)

if __name__ == "__main__":
    main()