class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        visited = {beginWord}

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                cand = q.popleft()
                if cand == endWord:
                    return steps
                for word in wordList:
                    if word in visited:
                        continue
                    if self.canTransform(word, cand):
                        visited.add(word)
                        q.append(word)
        return 0

    def canTransform(self, word, candidateWord):
        cand_idx = 0
        not_equal = False
        for idx in range(len(word)):
            if candidateWord[cand_idx] != word[idx] and not_equal:
                return False
            elif candidateWord[cand_idx] != word[idx]:
                not_equal = True
            cand_idx += 1
        return True