from crossingMethods.simpleCross import simpleCross
from selectionMethods.eliteSelection import eliteSelection

class GeneticHelper:

    def getCrossMethod(self,usedCrossMethod):
        usedCrossMethod = usedCrossMethod.strip().upper()
        if(usedCrossMethod == 'SIMPLE'):
            return simpleCross
        else:
            return simpleCross

    def getSelectionMethod(self,usedSelectionMethod):
        usedSelectionMethod = usedSelectionMethod.strip().upper()
        if(usedSelectionMethod == 'ELITE'):
            return eliteSelection
        else:
            return eliteSelection