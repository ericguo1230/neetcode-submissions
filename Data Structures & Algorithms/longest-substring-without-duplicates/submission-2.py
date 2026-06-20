class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        characters = set()
        max_len = 0
        for i, e in enumerate(s):
            if e in characters:
                max_len = max(max_len, len(characters))
                while e in characters:
                    characters.remove(s[left])
                    left += 1
            characters.add(e)
        max_len = max(max_len, len(characters))
        return max_len