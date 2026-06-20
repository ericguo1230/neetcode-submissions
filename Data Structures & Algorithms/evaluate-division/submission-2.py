class DisjoinSet:
    def __init__(self):
        self.parent = {}
        self.convert = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.convert[x] = 1.0
    
    def find(self, x):
        if x != self.parent[x]:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.convert[x] *= self.convert[orig_parent]
        return self.parent[x]
    
    def union(self, x, y, value):
        self.add(x)
        self.add(y)
        x1, y1 = self.find(x), self.find(y)
        if x1 != y1:
            self.parent[x1] = y1
            self.convert[x1] = value * self.convert[y] /self.convert[x]
    
    def get_ratio(self, x, y):
        if x not in self.parent or y not in self.parent:
            return -1.0
        x1, y1 = self.find(x), self.find(y)
        if x1 != y1:
            return -1.0
        return self.convert[x] / self.convert[y]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = DisjoinSet()
        res = []
        for i, a in enumerate(equations):
            uf.union(a[0], a[1], values[i])
        
        for a, b in queries:
            res.append(uf.get_ratio(a, b))
        return res