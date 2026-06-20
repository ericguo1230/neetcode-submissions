class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[None] * n for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def bfs(root):
            q = deque()
            q.append((0, root))
            visited = set()
            visited.add(None)
            visited.add(root)

            maxHeight = 0
            while q:
                h, cur = q.popleft()
                visited.add(cur)
                maxHeight = max(maxHeight, h)
                for v in adj[cur]:
                    if v not in visited:
                        visited.add(v)
                        q.append((h + 1, v))
            return maxHeight
        
        minHeight = float('inf')
        dic = defaultdict(list)
        for i in range(n):
            h = bfs(i)
            minHeight = min(minHeight, h) 
            if h == minHeight:
                dic[h].append(i)
            
        return dic[min(dic)]
