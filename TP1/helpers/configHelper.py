import json
from hanoiTowers import HanoiTowers
from state import State

class ConfigHelper:
    
    possibleSearchMethods = tuple(['BPP','BPA','BPPV','HG','HL','A*'])
    possibleHeuristicFunctions = tuple(['FHF','SHF'])
    MIN_DISK_COUNT = 3
    MAX_DISK_COUNT = 7
    MAX_TOWERS_COUNT = 3
    
    def __init__(self):
            with open("./config/config.json","r") as config_file:
                data = json.load(config_file)
                ##Getting search properties 
                self.searchMethod = data['search_properties']['search_method']
                self.heuristicFunction = data['search_properties']['heuristic_function']
                ##Getting game properties
                self.diskCount = data['game_properties']['disk_count']
                self.destinationTower = data['game_properties']['destination_tower']
                hanoiTowers = HanoiTowers(self.diskCount,self.destinationTower,None)
                towers = list(data['game_properties']['initial_state'].values())
                self.initialState = State(towers,hanoiTowers.areWinningTowers(towers))

    def print(self):
        valid = self.validateConfigurationProperties()
        print("Parameters valid : "+str(valid))

    def validateConfigurationProperties(self):
        return self.__validateSearchProperties() and self.__validateGameProperties()

    def __validateSearchProperties(self):
        return self.__validateSearchMethod() and self.__validateHeuristicFunction()
        # return self.__validateSearchMethod()


    def __validateGameProperties(self):
        return self.__validateDiskCount() and self.__validateInitialState() and self.__validateDestinationTower()

    def __validateSearchMethod(self):
        isValid = self.searchMethod in self.possibleSearchMethods
        if(not isValid):
            print('Illegal search method used')
        return isValid
    
    def __validateHeuristicFunction(self):
        isValid = self.heuristicFunction in self.possibleHeuristicFunctions
        if(not isValid):
            print('Illegal heuristic function used')
        return isValid

    def __validateDiskCount(self):
        isValid = isinstance(self.diskCount,int) and self.diskCount >= self.MIN_DISK_COUNT and self.diskCount <= self.MAX_DISK_COUNT
        if(not isValid):
            print("Illegal disk count used : Should be a number between "+str(self.MIN_DISK_COUNT)+" and "+str(self.MAX_DISK_COUNT))
        return isValid

    def __validateInitialState(self):
        hanoiTowers = HanoiTowers(self.diskCount,self.destinationTower,None)
        isValid = hanoiTowers.validateState(self.initialState)
        if(not isValid):
            print("Illegal initial state")
        return isValid

    def __validateDestinationTower(self):
        isValid = isinstance(self.destinationTower,int) and self.destinationTower >=1 and self.destinationTower <=self.MAX_TOWERS_COUNT
        if(not isValid):
            print("Illegal destination tower : Should be a number between 1 and "+str(self.MAX_TOWERS_COUNT))
        return isValid


    
