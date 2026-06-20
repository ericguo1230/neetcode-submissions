class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        cur = self.root
        idx = -1
        for i, c in enumerate(word):
            if c not in cur.children:
                return idx
            cur = cur.children[c]
            if cur.end:
                idx = i
        return idx
            
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.insert(w)

        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)
            


