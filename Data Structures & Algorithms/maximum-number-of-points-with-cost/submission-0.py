class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [i for i in points[0]]
        for i in range(1, len(points)):
            temp_dp = [0] * len(points[0])
            for j in range(len(points[0])):
                res = 0
                for idx, d in enumerate(dp):
                    res = max(res, d + points[i][j] - self.subtractValue(idx, j))
                temp_dp[j] = res
            dp = temp_dp
        return max(dp)
    
    def subtractValue(self, c1, c2):
        return abs(c1 - c2)