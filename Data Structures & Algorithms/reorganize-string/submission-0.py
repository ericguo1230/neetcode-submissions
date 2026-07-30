class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        letter_cnt = Counter(s)
        char_arr = [(-value, key) for key, value in letter_cnt.items()]
        #Step 2: Check if most common character is over half (if so we return "")
        heapq.heapify(char_arr)
        if -char_arr[0][0] > math.ceil(len(s) / 2):
            return ""
        
        #Step 3: Iteratively take the most common char in our heap (if we previously used it, use the second most common)
        output = []
        while char_arr:
            val, cand = heapq.heappop(char_arr)
            if output and output[-1] == cand:
                val2, cand2 = heapq.heappop(char_arr)
                output.append(cand2)
                val2 += 1
                if val2 < 0:
                    heapq.heappush(char_arr, (val2, cand2))
            else:
                val += 1
                output.append(cand)

            if val < 0:
                heapq.heappush(char_arr, (val, cand))
        return "".join(output)
        