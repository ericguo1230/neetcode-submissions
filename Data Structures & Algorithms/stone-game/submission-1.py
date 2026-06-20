class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = set()

        total = sum(piles)
        target = math.ceil(total / 2)
        
        turns = len(piles) // 2
        dp.add((target, 0))

        for p in piles:
            newDp = set()
            for i in dp:
                newDp.add(i)
            for t, turn in dp:
                if turn > turns:
                    continue
                if t - p <= 0:
                    return True
                newDp.add((t - p, turn + 1))
            dp = newDp
        return False
                
                