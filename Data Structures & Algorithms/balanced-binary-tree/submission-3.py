# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxVal = -1
        minVal = 1000000
        
        if not root:
            return True

        def dfs(node, height):
            nonlocal maxVal, minVal

            print(node.val)
            if not node.right and not node.left:
                if height < minVal:
                    minVal = height
                if height > maxVal:
                    maxVal = height
                return
            if node.right:
                dfs(node.right, height + 1)
            if node.left:
                dfs(node.left, height + 1)
        
        dfs(root, 0)

        return maxVal - minVal <= 1
            
        