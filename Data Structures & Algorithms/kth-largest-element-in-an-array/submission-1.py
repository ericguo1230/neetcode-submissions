class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for n in nums:
            arr.append(-n)
        heapq.heapify(arr)
        while k > 1:
            heapq.heappop(arr)
            k -= 1
        return -heapq.heappop(arr)