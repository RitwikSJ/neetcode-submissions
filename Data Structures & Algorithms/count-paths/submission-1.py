cache = []
first = True

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        global first, cache
        if first:
            first = False
            cache = [[-1] * n for _ in range(m)]

            for i in range(len(cache)):
                for j in range(len(cache[0])):
                    if i == 0 or j == 0:
                        cache[i][j] = 1

        print(m, n, cache)
        
        if cache[m - 1][n - 1] != -1:
            return cache[m - 1][n - 1]
        
        # print(m, n, cache)
        
        cache[m - 1][n - 1] = self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)
        return cache[m - 1][n - 1]