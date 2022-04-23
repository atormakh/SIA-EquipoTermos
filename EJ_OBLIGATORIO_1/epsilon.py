class Epsilon:

    def __init__(self,reactives):
        self.reactives = reactives

    def __str__(self):
        return f'{{Reactives: {str(self.reactives)}}}'
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self,other):
        return self.reactives == other.reactives

    def __hash__(self):
        return hash(self.reactives)