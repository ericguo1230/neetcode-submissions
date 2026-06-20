class UnionSet():
    def __init__(self, n):
        self.rank = [1] * (n)
        self.parent = [i for i in range(n)]
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        pu = self.find(x)
        pv = self.find(y)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        u = UnionSet(ROWS * COLS)
        edges = []
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i + 1 < ROWS:
                    edges.append((abs(heights[i][j] - heights[i + 1][j]), i * COLS + j, (i + 1) * COLS + j))
                if j + 1 < COLS:
                    edges.append((abs(heights[i][j] - heights[i][j + 1]), i * COLS + j, i * COLS + j + 1))
        edges.sort()
        for w, x, y in edges:
            u.union(x, y)
            if u.find(0) == u.find(ROWS * COLS - 1):
                return w
        return 0
