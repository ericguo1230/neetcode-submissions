class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(turn, i, M):
            if i == len(piles):
                return 0
            if (turn, i, M) in dp:
                return dp[(turn, i, M)]
            
            res = 0 if turn else float('inf')
            totals = 0

            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                totals += piles[i + X - 1]
                if turn:
                    res = max(res, totals + dfs(not turn, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not turn, i + X, max(M, X)))
            dp[(turn, i, M)] = res
            return dp[(turn, i, M)]
        return dfs(True, 0, 1)