class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in range(len(coins)):
            tmp = dp[:]
            for i in range(1, amount + 1):
                coin_value = coins[coin]
                if coin_value > i:
                    tmp[i] = dp[i]
                else:
                    tmp[i] = tmp[i - coin_value] + dp[i]
            dp = tmp
        return dp[amount]
