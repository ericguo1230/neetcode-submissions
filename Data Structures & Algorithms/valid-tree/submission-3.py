class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for i in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = set()
        def dfs(v, par):
            if v in visit:
                return False

            visit.add(v)
            for i in adj[v]:
                if i == par:
                    continue
                if not dfs(i, v):
                    return False
            return True

        return dfs(0, None) and len(visit) == n
        
