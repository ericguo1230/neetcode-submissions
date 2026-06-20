class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        num = n
        while True:
            s = str(num)
            num = 0
            for c in s:
                num += int(c) ** 2
            if num == 1:
                return True
            if num in visit:
                break
            visit.add(num)
        return 1 in visit

