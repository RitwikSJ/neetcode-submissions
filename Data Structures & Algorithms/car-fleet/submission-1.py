class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        stack = []
        
        cars.sort(key=lambda x: x[0])
        print(cars)

        for i in range(len(cars) - 1, -1, -1):
            pos, spd = cars[i]
            if not stack:
                stack.append(cars[i])
            else:
                time_taken = (target - stack[-1][0]) / stack[-1][1]
                print(time_taken, stack[-1][1] * time_taken, target)
                if ((pos + spd * time_taken) < target):
                    stack.append(cars[i])
        
        return len(stack)



        