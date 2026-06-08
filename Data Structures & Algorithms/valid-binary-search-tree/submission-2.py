# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return True

        for parentVal, childType in self.stack:
            if childType == 0:
                if root.val >= parentVal:
                    return False
            elif root.val <= parentVal:
                return False
        
        self.stack.append([root.val, 0])
        if self.dfs(root.left):
            self.stack[-1] = [root.val, 1]
            if self.dfs(root.right):
                self.stack.pop()
                return True
        
        return False
        #print(root.val, self.dfs(root.left, root.val, 0), self.dfs(root.right, root.val, 1))
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.stack = []
        return self.dfs(root)
        