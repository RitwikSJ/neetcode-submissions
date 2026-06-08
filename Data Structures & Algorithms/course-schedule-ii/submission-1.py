class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = dict()
        inMap = dict()
        for curr, pre in prerequisites:
            if pre in adjMap:
                adjMap[pre].add(curr)
            else:
                adjMap[pre] = {curr}

            if curr in inMap:
                inMap[curr] += 1
            else:
                inMap[curr] = 1

        queue = set()
        order = []
        
        for i in range(numCourses):
            if i not in inMap:
                queue.add(i)
        
        while queue:
            curr = queue.pop()
            if curr in adjMap:
                for cls in adjMap[curr]:
                    if inMap[cls] == 1:
                        queue.add(cls)
                    else:
                        inMap[cls] -= 1
            order.append(curr)
        
        return order if len(order) == numCourses else []
        