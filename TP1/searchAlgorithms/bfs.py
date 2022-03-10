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
    colors=['#e4cfea', '#be93e9', '#bc93dd', '#9856c8']
    
    frontierNodes= deque()
    exploredStates= set()
    
    
    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game
    
    def start(self):
        graph = Network()
        graph.set_options("""var options = {
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "levelSeparation": 200,
      "nodeSpacing": 60,
      "direction": "UD",
      "sortMethod": "directed"
    }
  },
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }
}""")
        #graph.show_buttons(filter_=['physics','layout'])
        self.frontierNodes.append(self.tree.root)
        graph.add_node(hash(self.tree.root),physics=True,title=str(self.tree.root.state),label=str(self.tree.root.level),level=self.tree.root.level,y=0)
        while len(self.frontierNodes)>0:
            #graph.show("igol.html")
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.popleft()
            ## Si n no esta en los explorados, agregarlo
            if(not node.state in self.exploredStates):
                self.exploredStates.add(node.state)
                ## Si n esta etiquetado con un estado objetivo  #PREGUNTAR MANANA SI VA ANIDADO O NO
                if(node.state.isGoal):
                    solution = self.returnSolution(node)
                    graph.show("graph.html")
                    ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                    return solution
                ## Expandir el nodo n, guardando los sucesores en F y en A
                possibleMoves = self.game.possibleMoves(node.state)
                for move in possibleMoves:
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredStates):
                        graph.add_node(hash(auxNode),physics=True,title=str(auxNode.state),label=auxNode.level,level=auxNode.level,y=auxNode.level*100,color=('#7fe4b4' if auxNode.state.isGoal else self.colors[auxNode.level%4]))
                        graph.add_edge(hash(node) , hash(auxNode))
                        node.addChild(auxNode)
                        self.frontierNodes.append(auxNode)
        return None
                    
                    

    def returnSolution(self ,node ):
        #graph[hash(node)].color = '#7fe4b4'
        #graph.add_node(hash(node),physics=True,title=str(node.state),label=node.level,level=node.level,y=node.level*100,color='#7fe4b4')
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l