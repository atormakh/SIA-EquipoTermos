from helpers.configHelper import ConfigHelper

class GeneticHelper:

    def getCrossMethod(self,crossData):
        crossMethodClass = ConfigHelper.getCrossMethodClass(crossData["method"].strip().upper())
        return crossMethodClass.fromJson(crossData)

    def getMutationMethod(self,mutationData):
        mutationMethodClass = ConfigHelper.getMutationMethodClass(mutationData["method"].strip().upper())
        return mutationMethodClass.fromJson(mutationData)

    def getSelectionMethod(self,selectionData):
        selectionMethodClass = ConfigHelper.getSelectionMethodClass(selectionData["method"].strip().upper())
        return selectionMethodClass.fromJson(selectionData)

    def getFinishCondition(self,finishConditionData):
        finishConditionClass = ConfigHelper.getFinishConditionClass(finishConditionData["method"].strip().upper())
        return finishConditionClass.fromJson(finishConditionData)