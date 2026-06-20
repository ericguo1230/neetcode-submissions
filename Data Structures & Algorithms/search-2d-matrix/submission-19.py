class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1
        while bot <= top:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break
        if not (bot <= top):
            return False
        row = (top + bot) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = left + ((right - left)//2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False