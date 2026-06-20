class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        mp = defaultdict(list)
        for course, pre in prerequisites:
            mp[course].append(pre)
        
        def bfs(pre):
            visited = set()
            q = deque()
            q.append(pre)
            visited.add(pre)
            print(q, visited)
            while q:
                p = q.popleft()
                for pres in mp[p]:
                    if pres in mp and pres not in visited:
                        q.append(pres)
                        visited.add(pres)
                    if pres in visited:
                        return False
            return True

        for course in mp:
            for pre in mp[course]:
                if pre in mp:
                    res = bfs(pre)
                    if not res:
                        return False
        return True