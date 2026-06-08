# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return
        
        if not self.stack or root.val >= max(self.stack):
            self.res += 1
        
        self.stack.append(root.val)

        self.dfs(root.left)
        self.dfs(root.right)

        self.stack.pop()

    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.stack = []

        if not root:
            return 0
        
        self.dfs(root)
        return self.res



        