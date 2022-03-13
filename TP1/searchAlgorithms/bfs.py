from treeGraph import TreeGraph
from tree import Node , Tree
from collections import deque
import json
class Bfs:
    frontierNodes= deque()
    exploredStates= set()
    
    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game
    
    def start(self):
        treeGraph= TreeGraph()
        self.frontierNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        while len(self.frontierNodes)>0:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.popleft()
            ## Si n no esta en los explorados, agregarlo
            if(not node.state in self.exploredStates):
                self.exploredStates.add(node.state)
                ## Si n esta etiquetado con un estado objetivo  #PREGUNTAR MANANA SI VA ANIDADO O NO
          
                ## Expandir el nodo n, guardando los sucesores en F y en A
                possibleMoves = self.game.possibleMoves(node.state)
                for move in possibleMoves:
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredStates):
                        treeGraph.addNode(auxNode)
                        treeGraph.addEdge(node,auxNode)
                        node.addChild(auxNode)
                        self.frontierNodes.append(auxNode)

                    if(auxNode.state.isGoal):
                        solution = self.returnSolution(node)
                        treeGraph.show("graph.html")
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return solution 
                 
                  
                   
        return None
                    
                    

    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l