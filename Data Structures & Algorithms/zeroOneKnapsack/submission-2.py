class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def top_down(idx, cap):
            if cap == capacity or idx == len(profit):
                return 0
            
            if (cap, idx) in cache:
                return cache[(cap, idx)]
            
            res = top_down(idx + 1, capacity)
            for i in range(idx, len(weight)):
                if cap + weight[i] > capacity:
                    continue
                cap += weight[i]
                res = max(res, profit[i] + top_down(i + 1, cap))
                cap -= weight[i]
            cache[(cap, idx)] = res
            return res
        
        return top_down(0, 0)
                
