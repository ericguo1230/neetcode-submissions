class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i - 1 for i in range(n + 1)]
        dp[0] = 0
        for cand in range(1, n + 1):
            for j in range(cand - 2, 1, -1):
                dp[cand] = max(dp[cand], dp[cand-j] * j, j * (cand - j))
            print(dp)
        return dp[n]
