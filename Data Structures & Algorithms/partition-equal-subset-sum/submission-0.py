class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        
        target = target // 2
        dp = set()
        dp.add(target)

        for num in nums:
            new_dp = set()
            if num in dp:
                return True
            for t in dp:
                new_dp.add(t)
                new_dp.add(t - num)
            dp = new_dp

        return False
