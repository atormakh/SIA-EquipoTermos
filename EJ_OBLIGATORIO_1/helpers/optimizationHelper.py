from helpers.configHelper import ConfigHelper

class OptimizationHelper:

    def getOptimizationMethod(self,method):
        optimizationMethodClass = ConfigHelper.getOptimizationMethodClass(method.strip().upper())
        return optimizationMethodClass.getMethod()