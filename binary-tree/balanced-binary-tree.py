# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checker(root):
            if not root:
                return 0
            left = checker(root.left)
            right = checker(root.right)
            if abs(left - right) > 1:
                return -1
            return 1 + max(checker(root.left), checker(root.right))
        
        res = checker(root)
        if res == -1:
            return False
        else:
            return True
