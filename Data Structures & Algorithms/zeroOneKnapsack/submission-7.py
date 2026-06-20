class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [-1] * (M + 1)
        dp[0] = 0

        for idx in range(N):
            tmp = [-1] * (M + 1)
            tmp[0] = 0
            for c in range(1, M + 1):
                if c - weight[idx] >= 0 and dp[c - weight[idx]] != -1:
                    tmp[c] = max(tmp[c], profit[idx] + dp[c - weight[idx]])
            for idx, prof in enumerate(dp):
                tmp[idx] = max(tmp[idx], prof)
            dp = tmp[:]
        return max(dp)

                
