class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest, ind = 0, l
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
                ind = i
            l = r + 1
            r = farthest
            res += 1
        return res