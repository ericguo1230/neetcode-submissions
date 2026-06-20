class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                dp[j] += dp[j - coins[i]] if j - coins[i] >= 0 else 0
        return dp[amount]