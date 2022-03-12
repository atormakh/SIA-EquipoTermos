from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from state import State
from hanoiTowers import HanoiTowers
from helpers.configHelper import ConfigHelper
from helpers.searchHelper import SearchHelper

def main():
    print("proyectazo de SIA")

    ##Create the helpers
    configHelper = ConfigHelper()
    searchHelper = SearchHelper()

    ##First,check if parameters are ok
    if(configHelper.validateConfigurationProperties()):
        ##Get the heuristic function used
        heuristicFunction = searchHelper.getHeuristicFunction(configHelper.heuristicFunction,configHelper.diskCount,configHelper.destinationTower)
        ##Start the Hanoi with the specified disk count and the heuristic function
        hanoiTowers = HanoiTowers(configHelper.diskCount,configHelper.destinationTower,heuristicFunction)
        ##Get the search method used
        searchMethod = searchHelper.getSearchMethod(configHelper.searchMethod,configHelper.initialState,hanoiTowers)
        ##Start the game
        solution = searchMethod.start()
        if(solution is not None):
            for sol in solution:
                print(sol)
            print( "se llego en " + str(len(solution)))
        else:
            print('No solution was found :(')


    
    # ilegal_state = State([[3,2,1],[],[]],False)

    # hanoi_towers = HanoiTowers(3)
    # initial_state = hanoi_towers.generateInitialState() #State([tower1,tower2,tower3],False)
    # print(hanoi_towers.validateState(ilegal_state))
    # bfs = Dfs(initial_state,hanoi_towers)
    # solution = bfs.start()
    # for sol in solution:
    #     print(sol)
    # print( "se llego en " + str(len(solution)))
    # configHelper = ConfigHelper()
    # configHelper.print()




#Variable que existe 
## python3 app.py => settea el name a main ( para ejectuarlo )
## Si quiero un archivo que es una clase y lo intenta de usar main lo patea
if __name__ == "__main__":
    main()