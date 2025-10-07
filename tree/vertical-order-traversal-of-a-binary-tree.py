# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
    
        def dfs(node, row, col):
            if node:
                nodes.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        nodes.sort()
        
        result = []
        prev_col = float('-inf')
        
        for col, row, val in nodes:
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].append(val)
        
        return result

