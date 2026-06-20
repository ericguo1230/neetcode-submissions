class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for n in nums:
            colors[n] += 1

        idx = 0
        for i in range(len(nums)):
            while colors[idx] == 0:
                idx += 1
            nums[i] = idx
            colors[idx] -= 1