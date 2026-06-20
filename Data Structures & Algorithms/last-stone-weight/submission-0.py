class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        n = len(stones) - 1
        while len(stones) > 1:
            if stones[n] == stones[n-1]:
                stones.pop()
                stones.pop()
                n -= 2
            else:
                res = stones[n] - stones[n-1]
                stones.pop()
                stones.pop()
                n -= 2

                if stones and res >= stones[n]:
                    stones.append(res)
                    n += 1
                    continue
                elif not stones:
                    stones.append(res)
                    n = 0
                    continue
                for i, s in enumerate(stones):
                    if s > res:
                        stones.insert(i, res)
                        n += 1
                        break
        return stones[0] if stones else 0
