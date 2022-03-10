
class Node:
    children = []
    
    def __init__(self,parent,state):
        self.parent = parent
        self.state = state
        if(parent is None):
            self.level =0
        else:
            self.level =parent.level+1

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash(tuple([self.state,self.parent]))

    def createChild(self,state):
        self.children.add(Node(self,state))
    def addChild(self , child):
        self.children.append(child)

class Tree:
    def __init__(self, initialState):
        self.root = Node(None,initialState)


   
#     ____________
#   | key  , value |
#   | (3 2 1) , 9  |
#   | ____________ |


# ( 3 2 1) , newHeight
 
# if ( map.haskey(321) and map.get(321) > height )
#     reemplazo map.set(321 , value)
#     true ( mira el nodo)
# else
#     false (descarto el nodo)
   
 

    







        
                
                


        



