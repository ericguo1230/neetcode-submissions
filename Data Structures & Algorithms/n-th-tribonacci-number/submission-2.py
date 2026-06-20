class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n == 2 or n==1:
                return 1
            elif n == 1 or n==0:
                return 0
        res = [0] * (n + 1)
        res[0], res[1], res[2] = 0, 1, 1
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i- 3]
        return res[n]