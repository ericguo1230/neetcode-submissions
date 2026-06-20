import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower()
        for i in range(len(palin)//2):
            if palin[i] != palin[len(palin) - 1 - i]:
                return False
        return True
