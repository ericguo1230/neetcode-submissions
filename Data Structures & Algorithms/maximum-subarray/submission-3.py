class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for n in nums:
            if n > curSum + n:
                curSum = n
            else:
                curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub