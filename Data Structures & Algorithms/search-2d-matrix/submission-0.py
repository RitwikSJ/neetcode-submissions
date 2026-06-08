class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows = len(matrix)
        nCols = len(matrix[0])

        l, r = 0, nRows * nCols - 1

        while l <= r:
            m = l + ((r - l) // 2)
            currRow = m // nCols
            currCol = m - (currRow * nCols)

            print(m, currRow, currCol, matrix[currRow][currCol])

            if matrix[currRow][currCol] == target:
                return True
            elif matrix[currRow][currCol] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
        