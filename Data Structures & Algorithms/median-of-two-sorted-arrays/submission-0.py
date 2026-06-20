class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_heap = []
        for num in nums1:
            heapq.heappush(total_heap, num)
        
        for num in nums2:
            heapq.heappush(total_heap, num)
        
        tot = len(total_heap)
        pop_amount = tot // 2
        last = None
        for i in range(pop_amount):
            last = heapq.heappop(total_heap)
        
        return total_heap[0] if tot % 2 == 1 else (total_heap[0] + last) / 2

        