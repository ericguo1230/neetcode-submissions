class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [costs[0][i] for i in range(3)]
        for i in range(1, len(costs)):
            temp_dp = [0] * 3
            for j in range(3):
                if j == 0:
                    temp_dp[j] = min(dp[1], dp[2]) + costs[i][0]
                elif j == 1:
                    temp_dp[j] = min(dp[0], dp[2]) + costs[i][1]
                else:
                    temp_dp[j] = min(dp[1], dp[0]) + costs[i][2]
            dp = temp_dp
        return min(dp)
