from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adjDict = dict()
        res = []
        nodesList = [None]

        dq = deque()
        dq.append(node)

        while dq:
            popAmt = len(dq)
            for i in range(popAmt):
                if str(dq[0].val) not in adjDict:
                    adjDict[str(dq[0].val)] = [neighbor.val for neighbor in dq[0].neighbors]
                    for neighbor in dq[0].neighbors:
                        if str(neighbor.val) not in adjDict:
                            dq.append(neighbor)
                dq.popleft()

        counter = 1
        while True:
            if str(counter) in adjDict:
                nodesList.append(Node(counter, None))
                counter += 1
            else:
                break
        
        counter = 1
        while True:
            if str(counter) in adjDict:
                nodesList[counter].neighbors = [nodesList[i] for i in adjDict[str(counter)]]
                counter += 1
            else:
                break
        
        return nodesList[1]




        