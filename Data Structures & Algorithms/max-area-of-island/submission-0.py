class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea, currArea = 0, 0

        def check_neighbors(row, col):
            nonlocal currArea
            currArea += 1
            grid[row][col] = 0
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                check_neighbors(row + 1, col)
            if col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
                check_neighbors(row, col + 1)
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                check_neighbors(row - 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                check_neighbors(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    check_neighbors(row, col)
                    if currArea > maxArea:
                        maxArea = currArea
                    currArea = 0
        
        return maxArea

        