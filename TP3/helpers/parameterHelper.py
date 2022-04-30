import re
from operator import truediv


class ParameterHelper:

    def __init__(self,trainSet , outputSet ):
        self.trainSet = trainSet
        self.outputSet = outputSet
        self.valid = True

    def __readFile(self , file):
        read = True
        list = []
        lineCount = None
        while read:
            line = file.readline()
            
            if not line:
                read = False
            else:
                line = re.sub(r"[\t\n]+", " ", line)
                line = re.sub(r"[\s]+" , " " , line )
                line = line.strip()
                line = line.split(' ')
                if not lineCount:
                    lineCount = len(line)
                else:
                    if(lineCount != len(line) ):
                        print('Invalid elem count')
                        return None
                for idx , e in enumerate(line):
                    line[idx] = float(e)
                list.append(line) 
        return list

    def readEntrenamineto(self):
        file = open(self.trainSet , 'r')
        entrenamiento = self.__readFile(file)
        file.close()
        return entrenamiento

    def readSalida(self):
        file = open(self.outputSet , 'r')
        salida = self.__readFile(file)
        file.close()
        return salida

    @staticmethod
    def validateParameters(trainSet , outputSet , shape):
        if(trainSet is None or outputSet is None):
            return False
        if( len(shape[0]) != len(trainSet[0])):
            return False

        if(len(shape[-1]) != len(outputSet[0])):
            return False