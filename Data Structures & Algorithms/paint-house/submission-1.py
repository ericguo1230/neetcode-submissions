class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [costs[0][i] for i in range(3)]
        for i in range(1, len(costs)):
            dp0 = min(dp[1], dp[2]) + costs[i][0]
            dp1 = min(dp[0], dp[2]) + costs[i][1]
            dp2 = min(dp[1], dp[0]) + costs[i][2]
            dp = [dp0, dp1, dp2]
        return min(dp)
