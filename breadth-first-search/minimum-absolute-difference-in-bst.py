# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum = [float('inf')]

        stack = [None]

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            if stack[0] is not None:
                minimum[0] = min(minimum[0], abs(node.val - stack[0]))
            
            stack[0] = node.val

            dfs(node.right)
        dfs(root)
        return minimum[0]



