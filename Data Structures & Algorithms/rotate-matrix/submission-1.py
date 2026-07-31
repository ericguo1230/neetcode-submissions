class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n // 2):
            for col in range(row, n - row - 1):
                # Top goes to right
                right = matrix[col][n - row - 1]
                matrix[col][n - row - 1] = matrix[row][col]

                # Right goes to bottom
                bottom = matrix[n - row - 1][n - col - 1]
                matrix[n - row - 1][n - col - 1] = right

                # Bottom goes to left
                left = matrix[n - col - 1][row]
                matrix[n - col - 1][row] = bottom

                # Left goes to top
                matrix[row][col] = left