# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = {}
        def bfs(node, l = 1):
            if not node:
                return
            
            level[l] = level.get(l, 0) + node.val
            bfs(node.left, l + 1)
            bfs(node.right, l + 1)
        bfs(root)

        max_sum = level[1]
        level_ = 1
        for k, sum in level.items():
            if sum > max_sum:
                max_sum = sum
                level_ = k
        return level_