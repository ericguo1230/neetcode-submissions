class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * m for i in range(n)]
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if cache[j][i] != -1:
                return cache[j][i]
            cache[j][i] = dfs(i + 1, j) + dfs(i, j + 1)
            return cache[j][i]
        return dfs(0, 0)