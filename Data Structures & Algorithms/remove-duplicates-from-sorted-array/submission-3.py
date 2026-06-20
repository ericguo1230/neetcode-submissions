class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = l = 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            l += 1
        return l