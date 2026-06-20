class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mp.values():
                stack.append(c)
            if c in mp:
                if not stack:
                    return False
                br = stack.pop()
                if mp[c] != br:
                    return False
        return not stack