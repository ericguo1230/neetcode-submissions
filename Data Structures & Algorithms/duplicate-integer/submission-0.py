class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyin = set()
        for i in nums:
            if i in alreadyin:
                return True
            alreadyin.add(i)
        return False