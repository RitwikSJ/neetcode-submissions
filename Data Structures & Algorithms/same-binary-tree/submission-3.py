# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    stack1 = []
    stack2 = []
    def dfs(self, root, num):
        val = root.val if root else None
        print("val", val)
        if num == 1:
            self.stack1.append(val)
        else:
            self.stack2.append(val)
        if root:
            self.dfs(root.left, num)
            self.dfs(root.right, num)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(p, q)
        self.stack1 = []
        self.stack2 = []
        self.dfs(p, 1)
        self.dfs(q, 2)

        print("new case?")
        print(self.stack1, self.stack2)
        return self.stack1 == self.stack2

        