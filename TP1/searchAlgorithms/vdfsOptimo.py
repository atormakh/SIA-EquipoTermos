from re import I
from treeGraph import TreeGraph
from tree import Node, Tree
from collections import deque
import math
class VdfsOptimo:

    
    solutionStates = dict() ## <heigth , State>
    exploredStates = dict() ## <State,heigth>
    frontierNodes = deque()
    discardedFrontier = deque() ## Los que borre por hmax (hojas no por repedito) 
    expandedNodesCount = 0
    frontierNodesCount = 1
    foundASolution = False

    def __init__(self,initialState,game , maxHeight):
        self.tree = Tree(initialState)
        self.game = game
        ## altura actual, cota izquierda , cota derecha
        self.maxHeight = maxHeight
        self.actualHeight = maxHeight 
        self.lowHeight = 0

    def start(self):
        treeGraph= TreeGraph()
        self.frontierNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolution(self.tree.root)
            treeGraph.show("graph.html")
            return solution
        return self.fixedHeightSearch(treeGraph)


    def fixedHeightSearch(self , treeGraph): 
        #print(f"actual:{self.actualHeight} , min:{self.lowHeight} , max:{self.maxHeight}")
        while len(self.frontierNodes)>0:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.pop()

            ## Si el nodo no esta explorado, o esta explorado en una profundidad mayor, explorarlo
            if(node.state.isGoal  and node.level <= self.actualHeight):
                self.frontierNodes.appendleft(node)
                return self.restart(treeGraph , True , node)

            if(node.level  < self.actualHeight ):
                if(not node.state in self.exploredStates or self.exploredStates[node.state] > node.level):
                    self.exploredStates[node.state] = node.level
                    ## Expandir el nodo n, guardando los sucesores en F y en A
                    self.expandedNodesCount+=1
                    possibleMoves = self.game.possibleMoves(node.state)
                    self.frontierNodesCount-=1
                    
                    goalNode = None

                    for move in possibleMoves:
                        self.frontierNodesCount+=1
                        ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                        auxNode = Node( node , move )
                        if(not auxNode in self.exploredStates):
                           # treeGraph.addNode(auxNode)
                            #treeGraph.addEdge(node,auxNode)
                            node.addChild(auxNode)
                            if(goalNode is None and auxNode.state.isGoal):
                                goalNode = auxNode
                            self.frontierNodes.append(auxNode)

                    if( goalNode is not None and goalNode.level <= self.maxHeight):
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        ## Como se encontro una solucion, se hace restart para buscar con altura maxima menor
                     #   if(not self.foundASolution)
                        return self.restart( treeGraph , True , goalNode) 
            else:
               #if(not self.foundASolution and node.level <= self.maxHeight ):
                    self.discardedFrontier.append(node)

        ## Como no se encontro una solucion, se hace restart para buscar con altura maxima mayor
        return self.restart(treeGraph , False)

    def restart(self , treeGraph , found , goalNode = None):
    #discard  [ a  b  c ] por altura estan esperando
    #frontier [ d  e  f ] me quedan para mirar (pero como dfs tienen baja prioridad)
    #nuevo frontier  [ a b c d e f ]  
        self.discardedFrontier += self.frontierNodes ##aca son el mismo objeto
        
        self.frontierNodes = self.discardedFrontier                
        self.discardedFrontier = deque() #aca cambio que discarded apunte a otro objeto
        print(f"En frontier nodes {len(self.frontierNodes)}")


        ##Si encontre una solucion, me fijo si es la optima, en caso de serlo la retorno, caso contrario realizo busqueda binaria
        if (found):
            self.solutionStates[goalNode.level] = goalNode.state
            self.foundASolution = True
            if(self.maxHeight == goalNode.level):
               self.lowHeight += 1
            
            self.maxHeight = goalNode.level #donde esta mi solucion 
                                            #uso el nuevo actual height
            self.actualHeight = math.floor((self.lowHeight + self.maxHeight )/2) #varia el actual

            print(f"found actual:{self.actualHeight} , min:{self.lowHeight} , max:{self.maxHeight} , con el goal en {goalNode.level}")
            #Encontre la solucion optimad
            if(self.actualHeight <= self.lowHeight): 
                print(self.solutionStates)
                solution = self.returnSolution(goalNode)
                treeGraph.show("graph.html")
                return solution
            
            
            return self.fixedHeightSearch(treeGraph)

        ##Si no encontre una solucion, y nunca lo hice hasta ahora, muevo mis indices para adelante para buscar mas profundo en el arbol mediante busqueda binaria
        if(not self.foundASolution):
            self.lowHeight = self.actualHeight ##ya se que no hay maximo en la primera parte
            self.actualHeight = self.incrementHeight()
            self.maxHeight = self.actualHeight
            return self.fixedHeightSearch(treeGraph)
        
        ##En caso de haber encontrado una solucion alguna vez, pero yendo para atras en el arbol no encontre ninguna, debo mover la cota menor y la actual para encontrar
        ##la solucion entre la minima y la maxima
        if(not found):
            print(f"not found: actual:{self.actualHeight} , min:{self.lowHeight} , max:{self.maxHeight}")
            self.lowHeight = self.actualHeight
            self.actualHeight = math.ceil((self.lowHeight + self.maxHeight )/2) #varia el actual
            return self.fixedHeightSearch(treeGraph)
            
           
    def incrementHeight(self):
        return self.actualHeight + 2 ##sqrt(2)
            
    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l 

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return self.frontierNodesCount
                