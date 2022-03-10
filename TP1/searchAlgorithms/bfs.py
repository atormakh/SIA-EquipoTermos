from tree import Node , Tree
from collections import deque
from pyvis.network import Network
#def graph():
#    net = Network()
#    net.add_node(0)
#    net.add_node(1)
#    net.add_edge(0,1)
#    net.show("igol.html")


class Bfs:

    frontierNodes= deque()
    exploredNodes= set()
    
    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game
    
    def start(self):
        graph = Network()

        self.frontierNodes.append(self.tree.root)
        graph.add_node(hash(self.tree.root),label=str(self.tree.root.level),level=self.tree.root.level,y=0)
        while len(self.frontierNodes)>0:
            #graph.show("igol.html")
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.popleft()
            ## Si n no esta en los explorados, agregarlo
            if(not node in self.exploredNodes):
                self.exploredNodes.add(node)
                ## Si n esta etiquetado con un estado objetivo  #PREGUNTAR MANANA SI VA ANIDADO O NO
                if(node.state.isGoal):
                    graph.show("graph.html")
                    ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                    return self.returnSolution(node)
                ## Expandir el nodo n, guardando los sucesores en F y en A
                possibleMoves = self.game.possibleMoves(node.state)
                for move in possibleMoves:
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredNodes):
                        graph.add_node(hash(auxNode),label=auxNode.level,level=auxNode.level,y=auxNode.level*100)
                        graph.add_edge(hash(node) , hash(auxNode))
                        node.addChild(auxNode)
                        self.frontierNodes.append(auxNode)
        return None
                    
                    

    def returnSolution(self ,node):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l