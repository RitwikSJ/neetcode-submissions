cache = []
first = True
final = None

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        global first, cache, final
        if first:
            first = False
            final = [m, n]
            cache = [[-1] * n for _ in range(m)]

            for i in range(len(cache)):
                for j in range(len(cache[0])):
                    if i == 0 or j == 0:
                        cache[i][j] = 1

        # print(m, n, len(cache), len(cache[0]))
        
        if cache[m - 1][n - 1] != -1:
            answer = cache[m - 1][n - 1]
            if [m, n] == final:
                print('resetting 2')
                cache = []
                first = True
                final = None

            return answer
        
        # print(m, n, len(cache), len(cache[0]))
        
        cache[m - 1][n - 1] = self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)

        answer = cache[m - 1][n - 1]
        if [m, n] == final:
            print('resetting 2')
            cache = []
            first = True
            final = None

        return answer