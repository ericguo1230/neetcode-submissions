class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for i in range(1, capacity + 1):
            for j in range(len(profit)):
                if weight[j] > i:
                    continue
                dp[i] = max(dp[i], dp[i - weight[j]] + profit[j])
        return dp[capacity]