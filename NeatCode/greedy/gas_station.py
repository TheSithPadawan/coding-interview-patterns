class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sum of gas needs to be at least the sum of cost
        if sum(gas) < sum(cost): return -1
        # if above line did not return -1, and the solution is unique
        # all below code was just finding out the starting point now.
        # if total running gas < 0, it cannot be the starting point, but part of the journey
        total = pos = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0 
                pos = i + 1
        return pos
# lc link: https://leetcode.com/problems/gas-station/
