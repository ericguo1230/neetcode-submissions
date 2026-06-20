class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] >= self.rank[py]:
            self.rank[px] += 1
            self.par[py] = px
        else:
            self.rank[py] += 1
            self.par[px] = py
        return True
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, e in emailGroup.items():
            res.append([accounts[i][0]] + sorted(e))
        return res


