# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        def helper(node, level):
            nonlocal levels
            if not node:
                return
            
            levels[level] = levels.get(level, []) + [node.val]
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        levels = {}
        helper(root, 0)
        res = []
        for i in range(len(levels) - 1, -1, -1):
            res.append(levels[i])
        return res
        