class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minIndex or val < self.stack[self.minIndex]:
            self.minIndex = len(self.stack) - 1
        print(self.minIndex)

    def pop(self) -> None:
        self.stack.pop()
        if self.minIndex == len(self.stack):
            if len(self.stack) == 0:
                self.minIndex = None
            else:
                minValue = self.stack[0]
                self.minIndex = 0
                for i in range(1, len(self.stack)):
                    if self.stack[i] < minValue:
                        self.minIndex = i

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        #print(self.stack, self.minIndex)
        return self.stack[self.minIndex]
        
