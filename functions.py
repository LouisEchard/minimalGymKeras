from enum import Enum

class explorationFunctions(Enum):
    fixed = 1



def getExplorationFunction(aChoice):
    if(aChoice == explorationFunctions.fixed):
        return fixedExploration




class fixedExploration:

    def getExplorationChance(self):

        return 1
