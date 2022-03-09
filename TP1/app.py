from state import State
from hanoiTowers import HanoiTowers
print("proyectazo de SIA")

tower1 = [7 , 6 ]
tower2= [ 5 , 4 , 3]
tower3= [2 , 1]


initial_state = State([tower1,tower2,tower3],False)

ilegal_state = State([[3,2,1],[],[]],False)

hanoi_towers = HanoiTowers()

print(hanoi_towers.validateState(ilegal_state))
for state in hanoi_towers.possibleMoves(initial_state):
    print(state.towers)

