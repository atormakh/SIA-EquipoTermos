import random

class Individual:
    
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
            gen = random.uniform(-self.maxRangeGen,self.maxRangeGen)
            genes.append(gen)
        return genes

    def __str__(self) -> str:
        return f"Individual:{{Genes: {str(self.genes)}}}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def strArrays(self) ->str:
        W = self.genes[0:3]
        w =[self.genes[3:6],self.genes[6:9]]
        w0 = self.genes[9:11]
        return f"""W={W}\n
                   \tw=[{w[0]}\n
                    \t  {w[1]}]\n
                   \tw0={w0}"""

    @classmethod
    def setupIndividualsMaxRangeGen(cls, maxRangeGen):
        cls.maxRangeGen = maxRangeGen