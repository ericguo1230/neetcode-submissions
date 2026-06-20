class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def top_down(cap, used):
            if cap == capacity:
                return 0
            
            if (cap, tuple(used)) in cache:
                return cache[(cap, tuple(used))]
            
            res = 0
            for i in range(len(weight)):
                if cap + weight[i] > capacity:
                    continue
                if i in used:
                    continue
                used.add(i)
                cap += weight[i]
                res = max(res, profit[i] + top_down(cap, used))
                used.remove(i)
                cap -= weight[i]
            cache[(cap, tuple(used))] = res
            return res
        
        return top_down(0, set())
                
