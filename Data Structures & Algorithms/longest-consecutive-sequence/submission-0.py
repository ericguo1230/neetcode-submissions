class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            count = 1
            if i - 1 not in nums:
                while i + 1 in nums:
                    i += 1
                    count += 1
                longest = max(count, longest)
        return longest
