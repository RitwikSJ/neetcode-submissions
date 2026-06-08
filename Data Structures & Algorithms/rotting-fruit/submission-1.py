from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        fresh = set()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    dq.append((row, col))
                    visited.add((row, col))
                elif grid[row][col] == 1:
                    fresh.add((row, col))
        
        mins = -1
        print(fresh)
        
        while dq and fresh:
            popAmt = len(dq)

            for i in range(popAmt):
                row, col = dq.popleft()

                if i != 0:
                    visited.add((row, col))

                if (row, col) in fresh:
                    fresh.remove((row, col))

                if row + 1 < len(grid) and (row + 1, col) not in visited and (row + 1, col) in fresh:
                    dq.append((row + 1, col))
                if row - 1 >= 0 and (row - 1, col) not in visited and (row - 1, col) in fresh:
                    dq.append((row - 1, col))
                if col + 1 < len(grid[0]) and (row, col + 1) not in visited and (row, col + 1) in fresh:
                    dq.append((row, col + 1))
                if col - 1 >= 0 and (row, col - 1) not in visited and (row, col - 1) in fresh:
                    dq.append((row, col - 1))
            
            print(fresh)
            mins += 1
        
        if not fresh:
            return max(mins, 0)
        return -1

