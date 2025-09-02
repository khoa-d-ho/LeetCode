# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(node, min, max):
            if not node:
                return True

            if node.val <= min or node.val >= max:
                return False

            return help(node.left, min, node.val) and help(node.right, node.val, max)

        return help(root, float("-inf"), float("inf"))

         