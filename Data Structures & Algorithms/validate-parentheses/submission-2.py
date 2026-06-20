class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in mp.values():
                stack.append(i)
            elif i in mp:
                if len(stack) == 0:
                    return False
                elif stack.pop() != mp[i]:
                    return False
        return len(stack) == 0