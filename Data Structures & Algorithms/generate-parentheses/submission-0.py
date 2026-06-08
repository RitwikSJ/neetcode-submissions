class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""

        def dfs(path, start, end):
            if start == end:
                path += "("
                dfs(path, start - 1, end)
            elif start == 0:
                while end:
                    path += ")"
                    end -= 1
                res.append(path)
            else:
                path += "("
                dfs(path, start - 1, end)
                path = path[:-1] + ')'
                dfs(path, start, end - 1)
        
        dfs(path, n, n)
        return res
        