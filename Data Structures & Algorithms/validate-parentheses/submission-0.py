class Solution:
    def isValid(self, s: str) -> bool:
        correspondenses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c not in correspondenses:
                stack.append(c)
            else:
                if len(stack) == 0 or correspondenses[c] != stack.pop():
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

