# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0.0]
        stack = deque([root])
        result = []
        while stack:
            n = len(stack)
            curr = 0
            for _ in range(n):
                new = stack.popleft()
                curr += new.val
                if new.left:
                    stack.append(new.left)
                if new.right:
                    stack.append(new.right)
            result.append(curr/n)
        return result
        