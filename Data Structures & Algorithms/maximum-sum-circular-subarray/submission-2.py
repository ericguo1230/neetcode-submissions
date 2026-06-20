class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [-float("inf")] * n
        prefixSum = 0
        rightMax[-1] = nums[-1]

        rightSum = nums[-1]
        for i in range(n - 2, -1, -1):
            rightSum += nums[i]
            rightMax[i] = max(rightSum, rightMax[i + 1])
        
        curMax, maxSum = 0, nums[0]
        for i in range(n):
            if curMax > 0:
                curMax += nums[i]
            else:
                curMax = nums[i]
            maxSum = max(maxSum, curMax, prefixSum + rightMax[i])
            prefixSum += nums[i]
        return maxSum