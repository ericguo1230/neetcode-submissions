class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        res = []
        for num in nums:
            mp[num] += 1
            if len(mp) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in mp.items():
                if c > 1:
                    new_count[num] = c - 1
            mp = new_count
        for n in mp:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res