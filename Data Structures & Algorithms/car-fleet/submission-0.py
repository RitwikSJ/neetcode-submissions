class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        stack = []
        
        cars.sort(key=lambda x: x[0])

        for i in range(len(cars)):
            pos, spd = cars[i]
            if not stack:
                stack.append(cars[i])
            else:
                time_taken = (target - pos) / spd
                print(time_taken, stack[-1][1] * time_taken, target)
                if ((stack[-1][0] + stack[-1][1] * time_taken) < target):
                    stack.append(cars[i])
                else:
                    stack.pop()
                    stack.append(cars[i])
        
        return len(stack)



        