class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        dist = {}  

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))

        return max(dist.values()) if len(dist) == n else -1

        