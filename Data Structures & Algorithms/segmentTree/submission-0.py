class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums) * 2)
        self.arr[len(self.arr) // 2:] = nums[:]
        self._buildTree()

    def _buildTree(self):
        for i in range(len(self.arr) // 2 - 1, 0, -1):
            self.arr[i] = self.arr[2 * i] + self.arr[2 * i + 1]
        
    def update(self, index: int, val: int) -> None:
        n = len(self.arr)
        diff = val - self.arr[index + n // 2]
        idx = index + n // 2
        while idx > 1:
            self.arr[idx] += diff
            idx //= 2
        self.arr[1] += diff

    
    def query(self, L: int, R: int) -> int:
        ans = 0
        L, R = L + len(self.arr) // 2, R + len(self.arr) // 2
        while L <= R:
            if (L & 1 == 1):
                ans += self.arr[L]
                L += 1
            if (R & 1 == 0):
                ans += self.arr[R]
                R -= 1
            L //= 2
            R //= 2
        return ans
