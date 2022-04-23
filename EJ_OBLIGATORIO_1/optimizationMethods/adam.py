

class Adam:

    def __init__(self):
        self.useGeneralAlgorithm = False

    def calculateOptimal(self,individual,function):
        return [0,0,0,0,0,0,0,0,0,0,0]

    def calculateDirection(self,individual):
        return None

    @classmethod
    def getMethod(cls):
        return cls()