from crossingMethods.simpleCross import simpleCross
from crossingMethods.uniformCross import uniformCross
from selectionMethods.eliteSelection import eliteSelection

class GeneticHelper:

    def getCrossMethod(self,usedCrossMethod):
        usedCrossMethod = usedCrossMethod.strip().upper()
        if(usedCrossMethod == 'SIMPLE'):
            return simpleCross
        elif(usedCrossMethod == 'UNIFORM'):
            return uniformCross
        else:
            return simpleCross

    def getSelectionMethod(self,usedSelectionMethod):
        usedSelectionMethod = usedSelectionMethod.strip().upper()
        if(usedSelectionMethod == 'ELITE'):
            return eliteSelection
        else:
            return eliteSelection