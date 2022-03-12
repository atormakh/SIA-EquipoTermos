
from treeGraph import TreeGraph
from tree import Node, Tree
from collections import deque

class LocalHeuristic:
    frontierNodes = deque()
    exploredStates = set()

    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game

    def start(self):
        treeGraph= TreeGraph()
        self.frontierNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        #Mientras L no este vacia
        while self.frontierNodes:
            #Considerar al nodo n de L cuyo estado tenga el menor valor de heuristica
            node = self.frontierNodes.popleft()
            #Si el estado no fue previamente explorado
            if(not node.state in self.exploredStates):
                # Expandir n de acuerdo a las acciones posibles para el estado que lo etiqueta
                possibleMoves = sorted(self.game.possibleMoves(node.state,True),key=lambda x: x.heuristic)
                # Formar una lista de nodos Lsucesores con los nodos obtenidos de la expansi´on de n.
                for move in possibleMoves:
                    auxNode= Node(node,move)
                    self.frontierNodes.append(auxNode)
                    node.addChild(auxNode)
                    treeGraph.addNode(auxNode)
                    treeGraph.addEdge(auxNode,node)
                    if(auxNode.state.isGoal):
                        #Fin de busqueda con exito.
                        solution = self.returnSolution(auxNode)
                        treeGraph.show("graph.html")
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return solution
    
    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l