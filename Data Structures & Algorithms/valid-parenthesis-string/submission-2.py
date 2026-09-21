class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        wildcard = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left > 0:
                    left -= 1
                elif wildcard > 0:
                    wildcard -= 1
                else:
                    print(1, i, left, wildcard)
                    return False
            else:
                wildcard += 1
        
        right = 0
        wildcard = 0
        
        for i in range(len(s) -1, -1, -1):
            if s[i] == ')':
                right += 1
            elif s[i] == '(':
                if right > 0:
                    right -= 1
                elif wildcard > 0:
                    wildcard -= 1
                else:
                    print(2, i, right, wildcard)
                    return False
            else:
                wildcard += 1
        
        return True