from helpers.configHelper import ConfigHelper

class GeneticHelper:

    def getCrossMethod(self,crossData):
        crossMethodClass = ConfigHelper.getCrossMethodClass(crossData["method"].strip().upper())
        return crossMethodClass.fromJson(crossData)

    def getSelectionMethod(self,selectionData):
        selectionMethodClass = ConfigHelper.getSelectionMethodClass(selectionData["method"].strip().upper())
        return selectionMethodClass.fromJson(selectionData)