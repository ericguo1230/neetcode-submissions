class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window of maintaining a totalSum >= target
        #once I am greater than target I can try to decrease my sliding window by moving my left pointer if my sum - the number at my
        #left pointer is still >= target

        currSum = 0
        left = 0
        minWindow = float('inf')
        for right in range(len(nums)):
            currSum += nums[right]
            while left < right and currSum - nums[left] >= target:
                currSum -= nums[left]
                left += 1
            minWindow = min(minWindow, right - left + 1) if currSum >= target else minWindow
        return minWindow if minWindow < float('inf') else 0