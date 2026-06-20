class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        sub = []
        def dfs(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        if nums:
            dfs(0)
        return res