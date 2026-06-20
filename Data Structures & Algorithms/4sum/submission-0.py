class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    tot = nums[i] + nums[j] + nums[left] + nums[right]
                    if tot > target:
                        right -= 1
                    elif tot < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                        while right > left and nums[left] == nums[left - 1]:
                            left += 1
        return res