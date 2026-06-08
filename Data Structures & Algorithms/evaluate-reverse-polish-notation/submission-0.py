import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for c in tokens:
            if c.isalnum():
                stack.append(int(c))
            else:
                stack.append(ops[c](stack.pop(), stack.pop()))
        
        return stack[0]


        