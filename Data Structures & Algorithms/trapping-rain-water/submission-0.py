class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        left_max = 0
        for i in range(1, n):
            left_max = max(left_max, height[i-1])
            left[i] = left_max
        
        right_max = 0
        for i in range(n - 2, -1, -1):
            right_max = max(right_max, height[i + 1])
            right[i] = right_max
        
        res = 0
        for i in range(n):
            if height[i] >= min(right[i], left[i]):
                continue
            res += min(right[i], left[i]) - height[i]
        return res