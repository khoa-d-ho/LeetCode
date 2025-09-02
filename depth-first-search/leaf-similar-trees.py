# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leafs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        elif root.left and not root.right:
            return self.get_leafs(root.left)
        elif root.right and not root.left:
            return self.get_leafs(root.right)
        else:
            return self.get_leafs(root.left) + self.get_leafs(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = self.get_leafs(root1)
        leafs2 = self.get_leafs(root2)

        return leafs1 == leafs2