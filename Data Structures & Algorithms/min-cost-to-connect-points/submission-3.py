class UnionSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x1, y1 = self.find(x), self.find(y)
        if x1 == y1:
            return False
        if self.rank[x1] > self.rank[y1]:
            self.parent[y1] = x1
        elif self.rank[x1] < self.rank[y1]:
            self.parent[x1] = y1
        else:
            self.parent[x1] = y1
            self.rank[y1] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        POINTS = len(points)
        edges = []
        u = UnionSet(POINTS)

        def manhattan_distance(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((manhattan_distance(points[i][0], points[i][1], points[j][0], points[j][1]), i, j))
        edges.sort()

        counter = 0
        res = 0
        for cost, x, y in edges:
            if counter == POINTS - 1:
                return res
            if not u.union(x, y):
                continue
            res += cost
            counter += 1
        return res
            