class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        
        for coin in range(len(coins)):
            dp[coin][0] = 1
            for i in range(1, amount + 1):
                coin_value = coins[coin]
                if coin_value > i:
                    dp[coin][i] = dp[coin - 1][i]
                else:
                    dp[coin][i] = dp[coin][i - coin_value] + dp[coin - 1][i]
        return dp[-1][amount]
