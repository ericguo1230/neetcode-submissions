class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_h, right_h = height[0], height[-1]
        res = 0
        while left < n - 1 and right > 0 and left <= right:
            if left_h > right_h:
                res += max(0, right_h - height[right])
                right -= 1
                right_h = max(right_h, height[right])
            else:
                res += max(0, left_h - height[left])
                left += 1
                left_h = max(left_h, height[left])
        return res