class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def check_neighbors(row, col):
            grid[row][col] = 0
            if row + 1 < len(grid) and grid[row + 1][col] == "1":
                check_neighbors(row + 1, col)
            if col + 1 < len(grid[row]) and grid[row][col + 1] == "1":
                check_neighbors(row, col + 1)
            if row - 1 >= 0 and grid[row - 1][col] == "1":
                check_neighbors(row - 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == "1":
                check_neighbors(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    check_neighbors(row, col)
                    total += 1
        
        return total

        