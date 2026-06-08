class Node:
    def __init__(self, value):
        self.value = value
        self.before = []
        self.after = []
    
    def updateBefore(self, node):
        self.before.append(node)
    
    def updateAfter(self, node):
        self.after.append(node)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = []
        for i in range(numCourses):
            courses.append(Node(i))
        
        for curr, prereq in prerequisites:
            courses[curr].updateBefore(courses[prereq])
            courses[prereq].updateAfter(courses[curr])
        
        visited = dict()
        time = 0
        loopPresent = False

        def dfs(currClass):
            nonlocal visited, time, loopPresent
            visited[currClass.value] = time

            if loopPresent:
                return
            
            for cls in currClass.after:
                if cls.value in visited and visited[cls.value] == time:
                    loopPresent = True
                    return
                dfs(cls)
        
        for cls in courses:
            if loopPresent:
                return False
            print(cls.value, cls.before)
            if cls.value not in visited and len(cls.before) == 0:
                dfs(cls)
                time += 1
        
        print(visited, time)
        return len(visited) == numCourses and not loopPresent

        