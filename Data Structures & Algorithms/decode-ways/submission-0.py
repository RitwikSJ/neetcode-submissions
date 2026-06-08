class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or (s[-1] == '0' and int(s[len(s) - 2]) > 2):
            return 0
        
        dp1 = dict()

        #last is double digits
        dp2 = dict()

        dp1[0] = 1
        dp2[0] = 0

        for i in range(1, len(s)):
            dp1[i] = 0
            dp2[i] = 0

            if s[i] != '0':
                dp1[i] = (dp1[i - 1] + dp2[i - 1])

            if int(s[i - 1]) <= 2:
                dp2[i] = dp1[i - 1]
            elif s[i] == '0':
                return 0

        return dp1[len(s) - 1] + dp2[len(s) - 1]