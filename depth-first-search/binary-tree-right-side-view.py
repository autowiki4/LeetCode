# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        result = []
        while stack:
            n = len(stack)
            for i in range(n):
                new = stack.popleft()
                if i == 0:
                    result.append(new.val)
                if new.right:
                    stack.append(new.right)
                if new.left:
                    stack.append(new.left)
        return result