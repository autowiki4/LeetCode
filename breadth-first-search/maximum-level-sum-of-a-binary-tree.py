# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, maximal = 0, float('-inf') 
        q = deque([root])
        current = 0
        while q:
            current += 1
            length = len(q)
            curr = 0
            for i in range(length):
                node = q.popleft()
                curr += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr > maximal:
                maximal = curr
                level = current
        return level
