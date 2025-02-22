# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        
        # start position
        start = 0
        for i in range(len(gas)):
            # what's the differnce between gas and the cost.
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        
        return start
