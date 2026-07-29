class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        #Preprocess s so that each char points to idx of duplicate immediately to the left of it
        #-1 if no duplicates
        n = len(s)
        prev_idx = [-1] * n
        prev_seen = {}
        for idx, char in enumerate(s):
            if char in prev_seen:
                prev_idx[idx] = prev_seen[char]
            prev_seen[char] = idx
    

        #Sliding window (move right 1 by 1)
        #if my preprocessed arr != -1 and my left pointer < arr[curr_idx], I know duplicate is in my window and adjust left to arr[curr_idx] + 1
            #After each iteration compute current window size
            #res = max(curr_window, res)
        left = 0
        res = 1
        for right in range(n):
            idx_before = prev_idx[right]
            if idx_before != -1 and idx_before >= left:
                left = idx_before + 1
            curr_window = right - left + 1
            res = max(res, curr_window)
        return res