# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxcount = 0
        def dfs(node, isleft, count):
            nonlocal maxcount
            if not node:
                return
            maxcount = max(maxcount, count)
            if isleft:
                dfs(node.right, False, count + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, count+1)
                dfs(node.right, False, 1)
        if root:
            dfs(root.right, False, 1)
            dfs(root.left, True, 1)
        return maxcount