class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if (s1 == "" and s2 == "" and s3 == ""):
            return True
        
        memo = {}

        def dp(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                if k < len(s3) - 1:
                    if dp(i + 1, j, k + 1):
                        res = True
                else:
                    res = True
            
            if j < len(s2) and s2[j] == s3[k]:
                if k < len(s3) - 1:
                    if dp(i, j + 1, k + 1):
                        res = True
                else:
                    res = True
            
            memo[(i, j, k)] = res
            return res
        
        return dp(0, 0, 0)