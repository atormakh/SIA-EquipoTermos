import json
from hanoiTowers import HanoiTowers
from state import State
from os import listdir
from os.path import isfile, join

class ConfigHelper:
    
    possibleSearchMethods = tuple(['BPP','BPA','BPPV', 'BPPVO','HG','HL','A*','F'])
    possibleHeuristicFunctions = tuple(['FHF','SHF','THF'])
    MIN_DISK_COUNT = 3
    MAX_DISK_COUNT = 15
    MAX_TOWERS_COUNT = 3
    
    def __init__(self,configPath):
            with open(configPath,"r") as config_file:
                data = json.load(config_file)
                ##Getting search properties 
                self.searchMethod = data['search_properties']['search_method']
                
                if self.searchMethod == 'ALL':
                    self.isMulti = True
                    self.multi = self.__getAll()
                else:
                    self.isMulti = False 
                if 'heuristic_function' in data['search_properties']:
                    self.heuristicFunction = data['search_properties']['heuristic_function']
                else:
                    self.heuristicFunction = None

                if 'max_height_bppv' in data['search_properties']:
                    self.maxHeightBppv = data['search_properties']['max_height_bppv']
                else:
                    self.maxHeightBppv = None

                if 'growth_factor_bppv' in data['search_properties']:
                    self.growthFactorBppv = data['search_properties']['growth_factor_bppv']
                else:
                    self.growthFactorBppv = None

                if 'weight' in data['search_properties']:
                    self.weight = data['search_properties']['weight']
                else:
                    print('WEight not found')
                    self.weight=None

                ##Getting game properties
                self.diskCount = data['game_properties']['disk_count']
                self.destinationTower = data['game_properties']['destination_tower']
                hanoiTowers = HanoiTowers(self.diskCount,self.destinationTower,None)
                towers = list(data['game_properties']['initial_state'].values())
                self.initialState = State(towers,hanoiTowers.areWinningTowers(towers))

    def __str__(self):
        return f"\t-Search method : {self.searchMethod}\n\t-Heuristic function : {self.heuristicFunction}\n\t-Disk count : {self.diskCount}\n\t-DestinationTower : {self.destinationTower}\n\t-Initial state : {self.initialState}\n\t-BPPV starting height : {self.maxHeightBppv}\n\t-BPPV growth factor : {self.growthFactorBppv}\n\t"

    def __repr__(self) -> str:
        return self.__str__()

    def print(self):
        valid = self.validateConfigurationProperties()
        print("Parameters valid : "+str(valid))

    def validateConfigurationProperties(self):
        return self.__validateSearchProperties() and self.__validateGameProperties()

    def __validateSearchProperties(self):
      # return all(self.__validateSearchMethod(),self.__validateHeuristicFunction(),self.__validateMaxHeightBppv(),self.__validateGrowthFactorBppv())
       return self.__validateSearchMethod() and self.__validateHeuristicFunction() and self.__validateMaxHeightBppv() and self.__validateGrowthFactorBppv() and self.__validateRequiredParameters() and self.__validateWeight()
        # return self.__validateSearchMethod()


    def __validateGameProperties(self):
        return self.__validateDiskCount() and self.__validateInitialState() and self.__validateDestinationTower()

    def __validateSearchMethod(self):
        isValid = self.searchMethod in self.possibleSearchMethods
        if(not isValid):
            print('Illegal search method used')
        return isValid
    
    def __validateHeuristicFunction(self):
        if self.heuristicFunction is not None:
            isValid = self.heuristicFunction in self.possibleHeuristicFunctions
            if(not isValid):
                print('Illegal heuristic function used')
            return isValid
        return True

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

    def __validateMaxHeightBppv(self):
        if self.maxHeightBppv is not None:
            isValid = isinstance(self.maxHeightBppv,int) and self.maxHeightBppv > 0
            if(not isValid):
                print('Illegal max height for BPPV algorithm')
            return isValid
        return True

    def __validateGrowthFactorBppv(self):
        if self.growthFactorBppv is not None:
            isValid = isinstance(self.growthFactorBppv,int) and self.growthFactorBppv > 0
            if(not isValid):
                print('Illegal growth factor for BPPV algorithm')
            return isValid
        return True
    
    def __validateWeight(self):
        if self.weight is not None:
            isValid = self.weight > 0 and self.weight < 1
            if(not isValid):
                print("Weight must be between 0 and 1")
            return isValid
        return True

    def __validateRequiredParameters(self):
        if self.searchMethod in ['HG','HL','A*','F']:
            isValid = self.heuristicFunction is not None
            if(not isValid):
                print('A heuristic function is required to this method, add the field \"heuristic_function\" into your search options')
            if self.searchMethod in ['F']:
                isValid= isValid and self.weight is not None
            return isValid

        if self.searchMethod in ['BPPV', 'BPPVO']:
            isValid = self.growthFactorBppv is not None and self.maxHeightBppv is not None
            if(not isValid):
                print('the fields \"growth_factor_Bppv\" and \"max_height_bppv\" are required in the search options for the BPPV algorith family')
            return isValid
        return True
    
    def __getAll(self):
        onlyfiles = [f for f in listdir('./config/exampleConfigs') if isfile(join('./config/exampleConfigs', f))]
        print(f"levante{len(onlyfiles)} , {onlyfiles}")
        helpers = []
        for file in onlyfiles:
            helpers.append(ConfigHelper(f"./config/exampleConfigs/{file}"))

        return helpers