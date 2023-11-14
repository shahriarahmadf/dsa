class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        currentGas = 0
        currentStation = 0
        startingStation = 0

        while True:
            currentGas += gas[currentStation]

            if currentGas >= cost[currentStation]:
                currentGas -= cost[currentStation]

                if currentStation == len(gas) - 1:
                    currentStation = 0
                else:
                    currentStation += 1
                
                if currentStation == startingStation:
                    return startingStation
            else:
                currentGas = 0
                currentStation += 1
                startingStation = currentStation