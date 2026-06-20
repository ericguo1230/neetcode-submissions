class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mp = Counter(nums)
        n = len(mp)
        idx = 0
        for i in range(n):
            nums[i] = nums[idx]
            idx += mp[nums[i]]
        return n