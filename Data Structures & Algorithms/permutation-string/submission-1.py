class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        mp = {}
        s1_mp = {}
        for s in s1:
            s1_mp[s] = s1_mp.get(s, 0) + 1
        for right in range(len(s2)):
            mp[s2[right]] = mp.get(s2[right], 0) + 1
            if right - left + 1 > len(s1):
                mp[s2[left]] -= 1
                if mp[s2[left]] <= 0:
                    mp.pop(s2[left])
                left += 1
            if right - left + 1 == len(s1) and mp == s1_mp:
                return True
        return False


