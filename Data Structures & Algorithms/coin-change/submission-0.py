class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)

        while q:
            p, l = q.popleft()
            if p == 0:
                return l
            for coin in coins:
                cur = p - coin
                if cur >= 0 and cur not in visited:
                    q.append((cur, l + 1))
                    visited.add(cur)
        return -1

            
            