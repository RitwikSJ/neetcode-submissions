class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                while stack:
                    if temperatures[i] > stack[-1][1]:
                        final[stack[-1][0]] = i - stack[-1][0]
                        stack.pop()
                    else:
                        break
                stack.append((i, temperatures[i]))
        
        return final
