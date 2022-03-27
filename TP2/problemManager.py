
class ProblemManager:

    REACTIVE_COUNT = 3
    EPSILON_SIZE = 3
    
    def __init__(self,epsilon,c):
        self.epsilon = epsilon
        self.c = c

    def validateEpsilon(self):
        #Primero, checkeamos que la cantidad de reactivos sea la requerida
        if(len(self.epsilon.reactives)!= self.REACTIVE_COUNT):
            return False
        
        #Luego, por cada reactivo, checkeamos que la cantidad sea correspondiente, y que cada elemento sean numeros decimales
        for reactive in self.epsilon.reactives:
            reactiveSize = len(reactive)
            if(reactiveSize!=self.EPSILON_SIZE):
                return False
            for reactiveValue in reactive:
                if(not isinstance(reactiveValue,float)):
                    return False
        return True

    def validateC(self):
        #Primero, checkeamos que la cantidad de resultados sea igual a la cantidad de reactivos
        if(len(self.c)!=self.REACTIVE_COUNT):
            return False
        
        #Luego, por cada resultado, validamos que sea un numero entero, y valga 0 o 1
        for resultValue in self.c:
            if(not isinstance(resultValue,int) or not (resultValue == 0 or resultValue == 1)):
                return False
        
        return True