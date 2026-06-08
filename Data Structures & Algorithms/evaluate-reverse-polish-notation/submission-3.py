import operator
import math

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
            if c.isalnum() or len(c) > 1:
                stack.append(int(c))
            else:
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(int(ops[c](arg2, arg1)))
        
        return stack[0]


        