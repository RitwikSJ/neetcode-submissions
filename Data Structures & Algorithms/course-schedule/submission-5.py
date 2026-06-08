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
        
        visited = set()
        pathSet = set()

        def dfs(currClass):
            nonlocal visited, pathSet

            if currClass.value in pathSet:
                return True
            elif currClass.value in visited:
                return False
            
            visited.add(currClass.value)
            pathSet.add(currClass.value)
            
            for cls in currClass.after:
                if dfs(cls): return True
            
            pathSet.remove(currClass.value)
            return False
        
        for cls in courses:
            if len(cls.before) == 0:
                if dfs(cls): return False
        
        return len(visited) == numCourses

        