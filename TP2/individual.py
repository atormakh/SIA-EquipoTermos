import random

class Individual:
    
    MIN_RANGE_PROPERTY = -10
    MAX_RANGE_PROPERTY = 10
    NUMBER_OF_GENES = 11

    #Crear individuo con genes determinados
    def __init__(self,genes=None):
        if( genes is None):
            self.genes = self.__generate__genes__random()
        else:
            self.genes = genes
    def __generate__genes__random(self):
        genes = []
        for i in range(0,self.NUMBER_OF_GENES):
            gen = random.uniform(self.MIN_RANGE_PROPERTY,self.MAX_RANGE_PROPERTY)
            genes.append(gen)
        return genes

    def __str__(self) -> str:
        return f"Individual:{{Genes: {str(self.genes)}}}"
    
    def __repr__(self) -> str:
        return self.__str__()