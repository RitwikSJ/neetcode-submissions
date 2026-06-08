# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
l = set()

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global l

        if not root:
            return True

        def dfs(node, height):
            print(node.val)
            if not node.right and not node.left:
                l.add(height)
                return
            if node.right:
                dfs(node.right, height + 1)
            if node.left:
                dfs(node.left, height + 1)
        
        dfs(root, 0)

        print(type(l))

        l = list(l)

        return max(l) - min(l) <= 1
            
        