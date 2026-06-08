class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ATLANTIC_ROW = len(heights)
        ATLANTIC_COL = len(heights[0])
        PACIFIC_ROW, PACIFIC_COL = -1, -1

        paths_found = [[[False, False] for j in range(len(heights[0]))] for i in range(len(heights))]

        res = set()
        visited = set()

        def dfs(first, last):
            nonlocal visited
            if not visited and first != last:
                return
            else:
                visited.add(last)

            if first == (0, 2):
                print('a', first)
                print('b', visited)
                print('c', last)
            
            row, col = last

            if row + 1 == ATLANTIC_ROW or col + 1 == ATLANTIC_COL:
                # if (0, 0) in visited:
                #     print('a', first)
                #     print('b', visited)
                #     print('c', last)
                for i, j in visited:
                    paths_found[i][j][1] = True
                if paths_found[first[0]][first[1]] == [True, True]:
                    res.add(first)
                    visited = set()
                    return
            
            if row - 1 == PACIFIC_ROW or col - 1 == PACIFIC_COL:
                # if (0, 0) in visited:
                #     print('a', first)
                #     print('d', visited)
                #     print('e', last)
                for i, j in visited:
                    paths_found[i][j][0] = True
                if paths_found[first[0]][first[1]] == [True, True]:
                    res.add(first)
                    visited = set()
                    return
            
            if row - 1 > PACIFIC_ROW and (row - 1, col) not in visited and heights[row][col] >= heights[row - 1][col]:
                dfs(first, (row - 1, col))
                # if visited:
                #     visited.remove((row - 1, col))
                # else:
                #     return
                if not visited:
                    return
            if row + 1 < ATLANTIC_ROW and (row + 1, col) not in visited and heights[row][col] >= heights[row + 1][col]:
                dfs(first, (row + 1, col))
                # if visited:
                #     visited.remove((row + 1, col))
                # else:
                #     return
                if not visited:
                    return
            if col + 1 < ATLANTIC_COL and (row, col + 1) not in visited and heights[row][col] >= heights[row][col + 1]:
                dfs(first, (row, col + 1))
                # if visited:
                #     visited.remove((row, col + 1))
                # else:
                #     return
                if not visited:
                    return
            if col - 1 > PACIFIC_COL and (row, col - 1) not in visited and heights[row][col] >= heights[row][col - 1]:
                dfs(first, (row, col - 1))
                # if visited:
                #     visited.remove((row, col - 1))
                # else:
                #     return
                if not visited:
                    return
            
            visited.remove(last)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if paths_found[i][j] != [True, True]:
                    dfs((i, j), (i, j))

        # print(paths_found)
        
        return [list(i) for i in res]





        