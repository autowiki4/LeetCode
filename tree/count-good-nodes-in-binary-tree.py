# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr = root.val
        count = [0]
        def dfs(node, new):
            if node.val >= new:
                count[0] += 1
            current = max(node.val, new)
            if node.left:
                dfs(node.left, current)
            if node.right:
                dfs(node.right, current)
        dfs(root, curr)
        return count[0]
