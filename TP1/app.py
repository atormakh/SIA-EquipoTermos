from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from state import State
from hanoiTowers import HanoiTowers

def main():
    print("proyectazo de SIA")
    ilegal_state = State([[3,2,1],[],[]],False)

    hanoi_towers = HanoiTowers(3)
    initial_state = hanoi_towers.generateInitialState() #State([tower1,tower2,tower3],False)
    print(hanoi_towers.validateState(ilegal_state))
    bfs = Bfs(initial_state,hanoi_towers)
    solution = bfs.start()
    for sol in solution:
        print(sol)
    print( "se llego en " + str(len(solution)))



#Variable que existe 
## python3 app.py => settea el name a main ( para ejectuarlo )
## Si quiero un archivo que es una clase y lo intenta de usar main lo patea
if __name__ == "__main__":
    main()