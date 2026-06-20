class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        idx = 0
        for c in s:
            if c == '(':
                stack.append(idx)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    continue
            res.append(c)
            idx += 1
        
        ans = deque([])
        for i in range(len(res) - 1, -1, -1):
            if stack and i == stack[-1]:
                stack.pop()
                continue
            ans.appendleft(res[i])
        return "".join(ans)
            