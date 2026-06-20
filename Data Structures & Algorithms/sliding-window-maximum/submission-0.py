class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        maxs = []
        for i in range(k):
            mp[nums[i]] += 1
            heapq.heappush(maxs, -nums[i])
        
        left = 0
        res = [-maxs[0]]
        for right in range(k, len(nums)):
            heapq.heappush(maxs, -nums[right])
            mp[nums[right]] += 1
            mp[nums[left]] -= 1
            if mp[nums[left]] == 0:
                del mp[nums[left]]
            left += 1
            while maxs and -maxs[0] not in mp:
                heapq.heappop(maxs)
            res.append(-maxs[0])
        return res
            