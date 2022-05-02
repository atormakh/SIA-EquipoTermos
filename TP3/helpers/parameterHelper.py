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
                        return None
                for idx , e in enumerate(line):
                    try:
                        line[idx] = float(e)
                    except ValueError:
                        return None
                list.append(line) 
        return list

    def readTrainingSetFile(self):
        file = open(self.trainSet , 'r')
        trainingSet = self.__readFile(file)
        file.close()
        return trainingSet

    def readResultSetFile(self):
        file = open(self.outputSet , 'r')
        resultSet = self.__readFile(file)
        file.close()
        return resultSet

    @staticmethod
    def validateParameters(trainingSet , resultSet , shape):
        # print('trainingSet before validations ==',trainingSet)
        # print('resultSet before validations ==',resultSet)
        if(trainingSet is None or resultSet is None):
            print("Illegal training and result set: Every element of each set must have the same count of items, and must be an integer or decimal number")
            return False
        # print('shape == ',shape)
        # print('trainSet == ',trainingSet)
        # print('trainSet[0] == ',len(trainingSet[0]))
        # print('shape[0]==',shape[0])
        # print('len(trainSet)==',len(trainingSet))
        # print('len(outputSet)==',len(resultSet))
        if( shape[0] != len(trainingSet[0])):
            print("Illegal training set: Length of elements do not match with architecture")
            return False
        if(shape[-1] != len(resultSet[0])):
            print("Illegal result set: Length of elements do not match with architecture")
            return False

        trainingSetLength = len(trainingSet)
        resultSetLength = len(resultSet)
        if(trainingSetLength!=resultSetLength):
            print("Illegal training and result set: There must be a result for each element in training set")
            return False
        return True 