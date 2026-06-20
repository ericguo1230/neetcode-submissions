class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        total = sum(piles)
        target = math.ceil(total / 2)
        
        def dfs(i, tot, turn):
            if i == len(piles) or tot >= target:
                return tot >= target
            if (i, tot, turn) in dp:
                return dp[(i, tot, turn)]
            if turn:
                dp[(i, tot, turn)] = dfs(i + 1, tot, turn) or dfs(i, tot + piles[i], not turn)
            else:
                dp[(i, tot, turn)] = dfs(i + 1, tot, turn) or dfs(i + 1, tot, not turn)
            return dp[(i, tot, turn)]
        return dfs(0, 0, True)