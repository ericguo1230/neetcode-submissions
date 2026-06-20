class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        adj = [[] for i in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        res = 0
        for v1 in range(len(adj)):
            q = deque()
            q.append(v1)
            init = len(visit)
            visit.add(v1)
            while q:
                v = q.popleft()
                for n in adj[v]:
                    if n not in visit:
                        visit.add(n)
                        q.append(n)
            if len(visit) > init:
                res += 1
        return res
                
        

        
