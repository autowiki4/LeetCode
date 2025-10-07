# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        def dfs(node, order):
            if not node:
                return
            if not node.left and not node.right:
                order.append(node.val)
            else:
                if node.left:
                    dfs(node.left, order)
                if node.right:
                    dfs(node.right, order)
        dfs(root1, r1)
        dfs(root2, r2)
        if len(r1) != len(r2):
            return False
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False
        return True
