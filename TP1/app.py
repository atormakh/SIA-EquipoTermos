from helpers.treeGraphHelper import TreeGraphHelper
from output import Output
from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from state import State
from hanoiTowers import HanoiTowers
from helpers.configHelper import ConfigHelper
from helpers.searchHelper import SearchHelper
import time

def main():
    print("proyectazo de SIA")

    ##Create the helpers
    configHelper = ConfigHelper()
    searchHelper = SearchHelper()

    ##First,check if parameters are ok
    if(configHelper.validateConfigurationProperties()):
        ##Get the heuristic function used
        heuristicFunction = searchHelper.getHeuristicFunction(configHelper.heuristicFunction,configHelper.diskCount,configHelper.destinationTower)
        maxHeightBppv = configHelper.maxHeightBppv
        growthFactorBppv = configHelper.growthFactorBppv

        ##Start the Hanoi with the specified disk count and the heuristic function
        hanoiTowers = HanoiTowers(configHelper.diskCount,configHelper.destinationTower,heuristicFunction)
        ##Get the search method used
        searchMethod = searchHelper.getSearchMethod(configHelper.searchMethod,configHelper.initialState,hanoiTowers,maxHeightBppv,growthFactorBppv)
        if(searchMethod is None):
            print(f'Error: could not recognize search method "{configHelper.searchmethod}"')
    
        initialTime=time.perf_counter()
        ##Start the game
        [tree,solution] = searchMethod.start()
        finishTime=time.perf_counter()
        ##Generate program output
        searchSucceded = solution is not None
        print("Generating Graph...")
        TreeGraphHelper(tree,solution)
        solutionHeight = 0
        if(searchSucceded):
            solutionHeight = len(solution)-1
        output = Output(configHelper,searchSucceded,solutionHeight,solutionHeight,searchMethod.getExpandedNodesCount(),searchMethod.getFrontierNodesCount(),solution,finishTime-initialTime)
        output.printOutput()

#Variable que existe 
## python3 app.py => settea el name a main ( para ejectuarlo )
## Si quiero un archivo que es una clase y lo intenta de usar main lo patea
if __name__ == "__main__":
    main()