class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in mapping and mapping[target-nums[i]] != i:
                return [i, mapping[target-nums[i]]]
        return []