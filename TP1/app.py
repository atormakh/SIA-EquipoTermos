from helpers.treeGraphHelper import TreeGraphHelper
from output import Output
from hanoiTowers import HanoiTowers
from helpers.configHelper import ConfigHelper
from helpers.searchHelper import SearchHelper
import time
import argparse

def main():
    print("proyectazo de SIA")
    configPath="./config/config.json"
    isGraphing = False
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c','--configPath',dest='configPath')
        parser.add_argument('-g','--graph',action="store_true",default=False)
        args = parser.parse_args()
        if(args.configPath is not None):
            configPath=args.configPath
        isGraphing=args.graph
    except Exception as e:
        print("Error in command line arguments")
        print(e)
    
    ##Crear los helpers
    configHelper1 = ConfigHelper(configPath)
    
    if(not configHelper1.isMulti):
        configHelper1 = [configHelper1]
    else:
        configHelper1 = configHelper1.multi
    counter = 0
    graphs = []
    for configHelper in configHelper1:
        searchHelper = SearchHelper()
        ##Primero, chequear que los parametros esten ok
        if(configHelper.validateConfigurationProperties() ):
            ##Pedir la funcion heuristica utilizada
            heuristicFunction = searchHelper.getHeuristicFunction(configHelper.heuristicFunction,configHelper.diskCount,configHelper.destinationTower)
            maxHeightBppv = configHelper.maxHeightBppv
            growthFactorBppv = configHelper.growthFactorBppv
            weight=configHelper.weight
            ##Empezar el Hanoi con la cantidad especificada de discos y la funcion heuristica
            hanoiTowers = HanoiTowers(configHelper.diskCount,configHelper.destinationTower,heuristicFunction)
            ##Pedir el metodo de busqueda utilizado
            searchMethod = searchHelper.getSearchMethod(configHelper.searchMethod,configHelper.initialState,hanoiTowers,maxHeightBppv,growthFactorBppv,weight)
            if(searchMethod is None):
                print(f'Error: could not recognize search method "{configHelper.searchmethod}"')
            initialTime=time.perf_counter()
            ##Empezar el juego
            [tree,solution] = searchMethod.start()
            finishTime=time.perf_counter()
            ##Generar la salida del programa
            searchSucceded = solution is not None
            graphs.append((tree,solution , counter))
            counter += 1
            solutionHeight = 0
            if(searchSucceded):
                solutionHeight = len(solution)-1
            output = Output(configHelper,searchSucceded,solutionHeight,solutionHeight,searchMethod.getExpandedNodesCount(),searchMethod.getFrontierNodesCount(),solution,finishTime-initialTime)
            output.printOutput()
            output.writeToFile()

    if(isGraphing):
        print("Starting Graphs")
        for graph in graphs:
            TreeGraphHelper(graph[0] , graph[1] , graph[2])

#Variable que existe 
## python3 app.py => settea el name a main ( para ejectuarlo )
## Si quiero un archivo que es una clase y lo intenta de usar main lo patea
if __name__ == "__main__":
    main()