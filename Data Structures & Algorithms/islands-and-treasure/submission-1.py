from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(rows, cols):
            dist = 0
            dq = deque()
            dq.append((rows, cols))
            visited = {(rows, cols)}
            minCandidate = 2147483647

            while dq:
                popAmt = len(dq)
                for i in range(popAmt):
                    row = dq[0][0]
                    col = dq[0][1]

                    if not grid[row][col]:
                        grid[rows][cols] = dist
                        return
                    
                    if grid[row][col] != 2147483647:
                        if dist + grid[row][col] < minCandidate:
                            minCandidate = dist + grid[row][col]  
                    
                    if row + 1 < len(grid) and grid[row + 1][col] not in visited and grid[row + 1][col] != -1:
                        visited.add((row + 1, col))
                        dq.append((row + 1, col))
                    if col + 1 < len(grid[row]) and grid[row][col + 1] not in visited and grid[row][col + 1] != -1:
                        visited.add((row, col + 1))
                        dq.append((row, col + 1))
                    if row - 1 >= 0 and grid[row - 1][col] not in visited and grid[row - 1][col] != -1:
                        visited.add((row - 1, col))
                        dq.append((row - 1, col))
                    if col - 1 >= 0 and grid[row][col - 1] not in visited and grid[row][col - 1] != -1:
                        visited.add((row, col - 1))
                        dq.append((row, col - 1))
                    
                    dq.popleft()
                
                dist += 1

                if dist == minCandidate:
                    grid[rows][cols] = dist
                    return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2147483647:
                    bfs(row, col)
                