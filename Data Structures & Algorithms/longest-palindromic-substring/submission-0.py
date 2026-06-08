class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(1, len(s) - 1):
            #odd check

            l, r = i - 1, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            currLen = (r - 1) - (l + 1) + 1

            if currLen > len(longest):
                longest = s[l + 1:r]
            
            #even check

            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            currLen = (r - 1) - (l + 1) + 1

            if currLen > len(longest):
                longest = s[l + 1:r]
        
        return longest
        