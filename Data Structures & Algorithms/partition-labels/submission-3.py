class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        mp = {}
        for i, c in enumerate(s):
            if c in mp:
                mp[c][1] = i
            else:
                mp[c] = [i, i]
        i = 0
        while i < len(s):
            end = mp[s[i]][1]
            j = i
            while j <= end:
                end = max(end, mp[s[j]][1])
                j += 1
            res.append(end - i + 1)
            i = j
        return res