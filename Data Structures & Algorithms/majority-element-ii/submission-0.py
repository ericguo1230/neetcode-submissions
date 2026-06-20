class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        n = math.floor(len(nums) / 3)
        res = []
        for num in mp:
            if mp[num] > n:
                res.append(num)
        return res