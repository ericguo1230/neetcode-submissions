class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def top_down(idx, cap):
            if cap == capacity or idx == len(profit):
                return 0
            
            if (cap, idx) in cache:
                return cache[(cap, idx)]
            
            res = top_down(idx + 1, cap)
            if cap + weight[idx] <= capacity:
                tmp = cap + weight[idx]
                res = max(res, profit[idx] + top_down(idx + 1, tmp))
            cache[(cap, idx)] = res
            return res
        
        return top_down(0, 0)
                
