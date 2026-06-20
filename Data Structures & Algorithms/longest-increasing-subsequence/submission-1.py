class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1000 + 1)
        res = 0
        for i in nums:
            i = i + 1000
            dp[i] = max(dp[:i]) + 1 if i != 0 else 1
            res = max(dp[i], res)
        return res
