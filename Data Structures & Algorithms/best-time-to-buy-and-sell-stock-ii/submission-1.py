class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buy):
            if i > len(prices) - 1:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            res = dfs(i + 1, buy)
            if buy:
                res = max(prices[i] + dfs(i + 1, not buy), res)
            else:
                res = max(res, -prices[i] + dfs(i + 1, not buy))
            dp[(i, buy)] = res
            return res
            
        return dfs(0, False)
            