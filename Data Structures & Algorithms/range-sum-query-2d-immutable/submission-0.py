class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = {}
        for row in range(len(matrix)):
            res = 0
            for col in range(len(matrix[0])):
                res += matrix[row][col]
                self.sums[(row, col)] = res
                if row > 0:
                    self.sums[(row,col)] += self.sums[(row - 1, col)]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box1, box2, box3 = 0, 0, 0
        res = self.sums[(row2, col2)]
        if row1 > 0:
            box2 = self.sums[(row1 - 1, col2)]
        if col1 > 0:
            box1 = self.sums[(row2, col1 - 1)]
        if row1 > 0 and col1 > 0:
            box3 = self.sums[(row1 - 1, col1 - 1)]
        print(box1, box2, box3, res)
        return res - (box1 + box2 - box3)
        

            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)