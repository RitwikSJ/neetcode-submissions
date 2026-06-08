# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            print(root.val, left, right)

            if left == -1 or right == -1:
                return -1
            
            if abs(left - right) > 1:
                print('wf')
                return -1

            return 1 + max(left, right)

        res = dfs(root)
        print(res)
        return res != -1         
        