import numpy as np

class Metrics:

    def __init__(self,classes,isNumbers,lowerBoundary,upperBoundary): 
        #Creamos la matriz de confusion en funcion de un array con las clases a analizar, y un diccionario de indices para modificar la misma
        classesLength = len(classes)
        dimension = (classesLength,classesLength)
        self.confussionMatrix = np.zeros(dimension)
        self.classesDict = dict()
        self.isNumbers = isNumbers
        self.lowerBoundary = lowerBoundary
        self.upperBoundary = upperBoundary
        for i in range(0,classesLength):
            classItem = classes[i]
            self.classesDict[classItem]=i

    def modifyConfussionMatrix(self,expectedArray,calculatedArray):
        #Recorremos el expectedArray y el calculated Array
        for i in range(0,len(expectedArray)):
            expectedValue = expectedArray[i]
            calculatedValue = calculatedArray[i]

            #Buscamos los indices de la fila y la columna a modificar de la matriz de confusion
            rowIndex = self.classesDict[self.__getExpectedValue(expectedValue)]
            columnIndex = self.__getClassIndex(calculatedValue)

            #Luego, incrementamos en 1 el casillero correspondiente de la matriz
            self.confussionMatrix[rowIndex][columnIndex]+=1

    def resetConfussionMatrix(self):
        classesLength = len(self.classesDict)
        dimension = (classesLength,classesLength)
        self.confussionMatrix = np.zeros(dimension)

    def getMetrics(self):
        #Primero, creamos un diccionario donde se devolveran el valor de las metricas correspondientes
        metricsDict = {'accuracy':0,'precision':0,'recall':0,'f_1-score':0,'true_positive_rate':0,'false_positive_rate':0}

        #Luego, checkeamos si la matriz de confusion es multiclase, ya que dependiendo de eso, se procedera distinto en el calculo de metricas
        isMulticlass = self.confussionMatrix.shape != (2,2)
        if(not isMulticlass):
            #Si no es multiclase, se calcula directo los valores de tp,tn,fp y fn, y se utilizan para el calculo de las metricas
            tp = self.confussionMatrix[0][0]
            fn = self.confussionMatrix[0][1]
            fp = self.confussionMatrix[1][0]
            tn = self.confussionMatrix[1][1]
            metricsDict['accuracy']=(tp+tn)/(tp+fn+fp+tn)
            metricsDict['precision'] = 0
            if((tp+fp)!=0):
                metricsDict['precision']=tp/(tp+fp)
            metricsDict['recall'] = 0
            metricsDict['true_positive_rate'] = 0
            if((tp+fn)!=0):
                metricsDict['recall']=tp/(tp+fn)
                metricsDict['true_positive_rate']=tp/(tp+fn)
            metricsDict['f_1-score'] = 0
            if(metricsDict['precision']+metricsDict['recall']!=0):
                metricsDict['f_1-score']=(2*metricsDict['precision']*metricsDict['recall'])/(metricsDict['precision']+metricsDict['recall'])
            metricsDict['false_positive_rate']
            if((fp+tn)!=0):
                metricsDict['false_positive_rate']=fp/(fp+tn)
        else:
            #Si es multiclase, por cada clase calculamos las metricas correspondientes, y las metricas totales resultan del promedio de las de cada clase
            for classItem in self.classesDict:
                (accuracy,precision,recall,score,truePositiveRate,falsePositiveRate) = self.__getMatricsByClass(classItem)
                metricsDict['accuracy']+=accuracy
                metricsDict['precision']+=precision
                metricsDict['recall']+=recall
                metricsDict['f_1-score']+=score
                metricsDict['true_positive_rate']+=truePositiveRate
                metricsDict['false_positive_rate']+=falsePositiveRate
            #Calculamos el promedio de todas las metricas
            metricsDict = {k: v / len(self.classesDict) for k, v in metricsDict.items()}

        return metricsDict


    def __getMatricsByClass(self,classItem):
        #Primero, buscamos el indice de la clase correspondiente
        classIndex = self.classesDict[classItem]

        #Luego calculamos los valores de tp,tn,fp y fn para dicha clase
        tp = self.confussionMatrix[classIndex][classIndex]
        fn = np.sum(self.confussionMatrix[classIndex]) - tp
        fp = self.confussionMatrix.sum(axis=0)[classIndex] - tp
        tn = np.sum(self.confussionMatrix) - (tp+fn+fp)

        #Una vez calculados dichos valores, calculamos las metricas en funcion de ellos 
        accuracy =(tp+tn)/(tp+fn+fp+tn)
        precision = 0
        if((tp+fp)!=0):
            precision=tp/(tp+fp)
        recall = 0
        truePositiveRate = 0
        if((tp+fn)!=0):
            recall=tp/(tp+fn)
            truePositiveRate=tp/(tp+fn)
        score = 0
        if(precision+recall!=0):
            score=(2*precision*recall)/(precision+recall)
        falsePositiveRate = 0
        if((fp+tn)!=0):
            falsePositiveRate=fp/(fp+tn)

        #Finalmente, retornamos el valor de las metricas
        return (accuracy,precision,recall,score,truePositiveRate,falsePositiveRate)

    def __getClassIndex(self,calculatedValueMatrix):
        classItem = None
        #Veamos si es el ejercicio de los numeros o no para obtener la clase de forma diferente
        if(not self.isNumbers):
            calculatedValue = calculatedValueMatrix.A[0][0]
            #Si no lo es, si el valor es menor a 0.5, corresponde al -1, y sino al 1
            classItem = 1
            if(calculatedValue<((self.lowerBoundary+self.upperBoundary)/2)):
                classItem = -1
        else:
            #Si es el ejercicio de los numero, tomamos como clase el indice el numero maximo
            calculatedValue = np.squeeze(np.asarray(calculatedValueMatrix))
            maxValue = max(calculatedValue)
            maxIndex = np.where(calculatedValue == maxValue)[0][0]
            # maxIndex = maxIndex[0][0]
            classItem = maxIndex
        #Finalmente, retornamos el indice correspondiente a la clase
        num = self.classesDict[classItem]
        return self.classesDict[classItem]

    def __getExpectedValue(self,expectedValueArray):
        if(not self.isNumbers):
           return expectedValueArray[0]
        #Si no es el ejercicio de los numeros, obtiene el valor esperado como el indice el elemento que vale 1
        return expectedValueArray.index(1)
        #[1]  [0 0 1 0 0 0 0]

        
        
    
    

# import numpy as np


# def initializeConfussionMatrix(classesCount=2):
    
#     #Creamos y devolvemos una matriz cuadrada de 0's, de dimension NxN, siendo N la cantidad de clases a distinguir (por default son 2)
#     dimension = (classesCount,classesCount)
#     return np.zeros(dimension)
    
    
#     # #Primero, creamos la matriz de metricas basica
#     # metricsMatrix = np.matrix(['TP','FN'],['FP','TN'])

#     # #Luego, retornamos una lista con dicha matriz, siendo el tamano de dicha lista la cantidad de clases requeridas
#     # metricsMatrices = []
#     # for i in range(0,classesCount):
#     #     metricsMatrices.append(metricsMatrix)

#     # #Finalmente, retornamos dicha lista junto con un diccionario de contadores para cada categoria
#     # metricsCounter = {'TP': 0,'FN': 0, 'FP': 0, 'TN':0}

#     # return (metricsMatrices,metricsCounter)




