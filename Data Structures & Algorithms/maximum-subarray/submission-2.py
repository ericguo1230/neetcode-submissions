class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, cur = nums[0], 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxSub = max(maxSub, cur)
        return maxSub