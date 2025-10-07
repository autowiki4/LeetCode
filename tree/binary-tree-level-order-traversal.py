# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        result = []

        while stack:
            n = len(stack)
            curr = []
            for _ in range(n):
                new = stack.popleft()
                curr.append(new.val)
                if new.left:
                    stack.append(new.left)
                if new.right:
                    stack.append(new.right)
            result.append(curr)
        return result