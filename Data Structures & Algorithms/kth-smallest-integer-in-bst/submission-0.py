# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root):
        if self.res is not None:
            return
        
        if root.left:
            self.dfs(root.left)
        
        if self.k == 1:
            self.res = root.val
            self.k -= 1
            return
        
        self.k -= 1

        if root.right:
            self.dfs(root.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.dfs(root)

        return self.res

        