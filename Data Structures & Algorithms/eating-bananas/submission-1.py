class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        max_pile = 0
        for i in piles:
            max_pile = max(max_pile, i)
        l, r = 1, max_pile
        res = r

        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
        return k