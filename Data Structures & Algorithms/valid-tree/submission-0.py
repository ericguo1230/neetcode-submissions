class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n:
            return False
        
        adj = [[] for _ in range(n)]

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visited = set()

        q = deque([(0, -1)])
        visited.add(0)
        while q:
            v, p = q.popleft()
            for i in adj[v]:
                if i == p:
                    continue
                if i in visited:
                    return False
                q.append((i, v))
                visited.add(i)
        return len(visited) == n
