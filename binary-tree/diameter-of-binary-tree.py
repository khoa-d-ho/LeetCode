# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            if not root:
                return 0
            nonlocal res # initiated outside
            l = dfs(root.left)
            r = dfs(root.right)

            res = max(res, l + r) # longest path of any two nodes

            return max(l, r) + 1 # remember to add 1

        dfs(root)
        return res