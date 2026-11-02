# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        heap = []

        def dfs(root):
            nonlocal res, heap

            if not root:
                return
            
            pushed = False
            if not heap or -heap[0] < root.val:
                heapq.heappush(heap, -root.val)
                pushed = True

            dfs(root.left)
            dfs(root.right)
            if pushed:
                heapq.heappop(heap)
            
            # print(root.val, heap)
            # if heap:
            #     print(-heap[-1], -heap[-1] <= root.val)
            
            if not heap or -heap[0] <= root.val:
                res += 1
        
        dfs(root)
        return res



        