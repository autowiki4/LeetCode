# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum, prefix):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix.get(curr_sum-targetSum, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            count += dfs(node.left, curr_sum, prefix)
            count += dfs(node.right, curr_sum, prefix)
            prefix[curr_sum] -= 1
            return count
        return dfs(root, 0, {0:1})