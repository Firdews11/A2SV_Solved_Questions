class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        zeroes_row = [0] * n
        zeroes_col = [0] * m
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    zeroes_row[row] = 1
                    zeroes_col[col] = 1
        for row in range(n):
            for col in range(m):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
