class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for i in prices:
            profit = max(profit, i - minimum)
            minimum = min(minimum, i)
        return profit