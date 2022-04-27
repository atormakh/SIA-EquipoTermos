
class LinealActivationFunction:

    def __init__(self):
        self.name = 'LINEAL'
    
    def apply(self,h):
        return 0 #TODO

    def applyDerivative(self,h):
        return 0 #TODO

    @classmethod
    def getType(cls):
        return cls()