class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k <= 1:
            return 0

        max_heap = [] #Keep track of smallest splits (k - 1)
        min_heap = [] #Keep track of highest splits (k - 1)

        #Iterate possible splits from [i to len(weights) - 2]
        #naively add to both heaps
        for idx in range(len(weights) - 1):
            split = weights[idx] + weights[idx + 1]
            if len(min_heap) < k - 1 or split > min_heap[0]:
                heapq.heappush(min_heap, split)
            if len(max_heap) < k - 1 or split > max_heap[0]:
                heapq.heappush(max_heap, -split)
            if len(min_heap) > k - 1:
                heapq.heappop(min_heap)
            if len(max_heap) > k - 1:
                heapq.heappop(max_heap)
        
        return sum(min_heap) + sum(max_heap)