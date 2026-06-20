class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        
        for n in nums:
            mp[n] += 1
            if len(mp) <= 2:
                continue
            new_mp = defaultdict(int)
            for num in mp:
                if mp[num] > 1:
                    new_mp[num] = mp[num] - 1
            mp = new_mp
        
        res = []
        for n in mp:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res