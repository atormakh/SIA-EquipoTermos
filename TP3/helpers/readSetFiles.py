import re
import math

def readNumberSetFiles(trainSetPath,outputSetPath):
    file = open(trainSetPath , 'r')
    trainingSet = __readNumbersFile(file)
    file.close()
    file = open(outputSetPath , 'r')
    resultSet = __readFile(file)
    file.close()
    return (trainingSet,resultSet)

def readSetFiles(trainSetPath,outputSetPath):
    file = open(trainSetPath , 'r')
    trainingSet = __readFile(file)
    file.close()
    file = open(outputSetPath , 'r')
    resultSet = __readFile(file)
    file.close()
    return (trainingSet,resultSet)

def __readFile(file):
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

def __readNumbersFile(file):
    read = True
    linesList = []
    numbersList = []
    lineCount = None
    numberOfColumns = 5
    numberOfRows = 7
    numbersIndex = 0
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
                #Valida que cada linea tenga 5 numeros
                if lineCount!=numberOfColumns:
                    return None
            else:
                if(lineCount != len(line) ):
                    return None
            for idx , e in enumerate(line):
                try:
                    num = int(e)
                    if(num==0 or num==1):
                        line[idx]=float(num)
                    else:
                        return None
                except ValueError:
                    return None
            linesList.append(line)
            #Si la cantidad de lineas leidas es multiplo de la cantidad de lineas por nro, agregamos el numero correspondiente
            if(len(linesList)%numberOfRows==0):
                numbersList.append([float(numbersIndex)])
                numbersIndex+=1
    #Finalmente, si la cantidad de lineas totales es multiplo de la cantidad de lineas por nro, devolvemos la lista de los mismos. Caso contrario se retorna None
    if(len(linesList)%numberOfRows==0):
        return numbersList
    return None

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