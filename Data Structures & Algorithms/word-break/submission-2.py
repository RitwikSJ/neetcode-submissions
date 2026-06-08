class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = dict() 
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(s):
                dp[(i, j)] = True
                return True
            elif j == len(s) + 1:
                dp[(i, j)] = False
                return False
                        
            if s[i:j] in wordDict:
                if dfs(j, j + 1):
                    dp[(i, j)] = True
                    return True
            
            dp[(i, j)] = dfs(i, j + 1)
            return dp[(i, j)]
        
        return dfs(0, 1)