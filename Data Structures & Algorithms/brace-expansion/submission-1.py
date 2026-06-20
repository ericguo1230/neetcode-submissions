class Solution:
    def expand(self, s: str) -> List[str]:
        #Step 1: Process string
        words = []
        tmp = []
        use_tmp = False
        for c in s:
            if c == ',': continue
            if c == '{':
                use_tmp = True
                continue
            if c == '}':
                use_tmp = False
                words.append(tmp)
                tmp = []
                continue
            if use_tmp: tmp.append(c)
            else: words.append(c)

        res = []
        tmp = []
        def backtrack(idx):
            if idx == len(words):
                res.append("".join(tmp))
                return

            for cand in words[idx]:
                tmp.append(cand)
                backtrack(idx + 1)
                tmp.pop()
        
        backtrack(0)
        return res