class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        visit, cycle = set(), set()
        output = []

        for c, p in prerequisites:
            adj[c].append(p)

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True

            cycle.add(node)
            for p in adj[node]:
                if dfs(p) == False:
                    return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True

        for p in range(numCourses):
            if dfs(p) == False:
                return []
        return output

