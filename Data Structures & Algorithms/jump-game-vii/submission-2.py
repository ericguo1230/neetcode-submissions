class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[-1] = True

        if minJump > n - 1:
            return False
        if s[-1] == '1':
            return False
        
        for i in range(n - 2, -1, -1):
            if i + minJump > n - 1 or s[i] == '1':
                dp[i] = False
            elif i + maxJump >= n - 1:
                dp[i] = True
            elif True in dp[i + minJump:i+maxJump+1]:
                dp[i] = True
        return dp[0]
            

