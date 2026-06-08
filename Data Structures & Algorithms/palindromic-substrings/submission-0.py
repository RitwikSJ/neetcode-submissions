class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(1, len(s) - 1):
            #odd check

            l, r = i - 1, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        for i in range(0, len(s) - 1):
            #even check

            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        return count + len(s)