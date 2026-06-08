class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or (s[-1] == '0' and int(s[len(s) - 2]) > 2):
            return 0
        
        dp1 = dict()

        #last is double digits
        dp2 = dict()

        prev1 = 1
        prev2 = 0
        new1 = 1
        new2 = 0

        for i in range(1, len(s)):
            new1 = 0
            new2 = 0

            if s[i] != '0':
                new1 = (prev1 + prev2)

            if int(s[i - 1]) <= 1 or int(s[i - 1]) * 10 + int(s[i]) <= 26:
                new2 = prev1
            elif s[i] == '0':
                return 0
            
            prev1 = new1
            prev2 = new2

        return new1 + new2