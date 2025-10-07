# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        dummy = TreeNode()
        curr = dummy
        while stack:
            new = stack.pop()
            if new.right:
                stack.append(new.right)
                new.right = None
            if new.left:
                stack.append(new.left)
                new.left = None
            curr.right = new
            curr = curr.right
        

        