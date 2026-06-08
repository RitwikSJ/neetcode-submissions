class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i, j):
            if i == len(s):
                return True
            elif j == len(s) + 1:
                return False
            
            if s[i:j] in wordDict:
                if dfs(j, j + 1):
                    return True
            
            return dfs(i, j + 1)
        
        return dfs(0, 1)