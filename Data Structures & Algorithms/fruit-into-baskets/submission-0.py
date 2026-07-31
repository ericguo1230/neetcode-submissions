class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        seen = defaultdict(int)
        res = 0
        for right in range(len(fruits)):
            seen[fruits[right]] += 1
            if len(seen) <= 2:
                res = max(res, right - left + 1)
            else:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
        return res