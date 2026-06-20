class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        globalMin = globalMax = nums[0]
        curMax = curMin = 0

        total = sum(nums)

        for n in nums:
            if curMax > 0:
                curMax += n
            else:
                curMax = n
            
            if curMin < 0:
                curMin += n
            else:
                curMin = n
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        if globalMax < 0:
            return globalMax
        return max(globalMax, total-globalMin)