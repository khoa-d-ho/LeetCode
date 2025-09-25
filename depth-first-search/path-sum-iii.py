# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.res = 0

        def backtrack(curr_node, curr_sum):
            if not curr_node:
                return 
            curr_sum += curr_node.val
            if curr_sum == targetSum:
                self.res += 1

            backtrack(curr_node.left, curr_sum)
            backtrack(curr_node.right, curr_sum)

        def traverse(curr_node):
            if not curr_node:
                return
            backtrack(curr_node, 0)
            traverse(curr_node.left)
            traverse(curr_node.right)
        traverse(root)
        return self.res