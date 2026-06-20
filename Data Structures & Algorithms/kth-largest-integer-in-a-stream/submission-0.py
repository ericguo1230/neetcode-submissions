class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums = sorted(self.nums)
        print(nums)
        if len(nums) < self.k:
            return nums[-1]
        return nums[len(nums) - self.k]