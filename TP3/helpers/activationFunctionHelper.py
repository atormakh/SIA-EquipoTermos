from helpers.configHelper import ConfigHelper

class ActivationFunctionHelper:

    def getActivationFunctionType(self,type,beta):
        activationFunctionClass = ConfigHelper.getActivationFunctionClass(type.strip().upper())
        return activationFunctionClass.getType(beta)