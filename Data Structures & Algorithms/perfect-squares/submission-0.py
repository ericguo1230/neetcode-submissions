class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0: 0}
        squares = set()
        for tot in range(1, n + 1):
            dp[tot] = dp[tot - 1] + 1
            root = math.sqrt(tot)
            if root.is_integer():
                dp[tot] = 1
                squares.add(tot)
            for square in squares:
                dp[tot] = min(dp[tot], dp[tot - square] + 1)
        return dp[n]
