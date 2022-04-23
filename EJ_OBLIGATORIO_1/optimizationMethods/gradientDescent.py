import numdifftools as nd

class GradientDescent:

    def __init__(self):
        self.useGeneralAlgorithm = True

    def calculateOptimal(self,individual,function):
        return [0,0,0,0,0,0,0,0,0,0,0]

    def calculateDirection(self,individual):
        return nd.Gradient(individual.genes)

    @classmethod
    def getMethod(cls):
        return cls()