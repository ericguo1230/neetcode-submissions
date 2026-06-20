class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gain = [i - j for i, j in zip(gas, cost)]
        if sum(gain) < 0:
            return -1
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += gain[i]
            if total < 0:
                total = 0
                res = i + 1
        return res