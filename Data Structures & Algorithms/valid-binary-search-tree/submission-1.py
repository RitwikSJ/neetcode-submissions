# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, parentVal, childType):
        if not root:
            return True
        if childType == 0:
            if root.val >= parentVal:
                return False
        elif root.val <= parentVal:
            return False
        
        return self.dfs(root.left, root.val, 0) and self.dfs(root.right, root.val, 1)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.val, 0) and self.dfs(root.right, root.val, 1)
        