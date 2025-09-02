# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checker(this, sub):
            if not this and not sub:
                return True
            if not this or not sub or this.val != sub.val:
                return False
            return checker(this.left, sub.left) and checker(this.right, sub.right)

        if not subRoot:
            return True
        if not root:
            return False
        if checker(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)