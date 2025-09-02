# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0
    def travel(self, node, count, left=True):
        if not node:
            return
        self.path = max(self.path, count)
        if left:
            self.travel(node.right, count + 1, False)
            self.travel(node.left, 1, True)
        else:
            self.travel(node.left, count + 1, True)
            self.travel(node.right, 1, False)


        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.travel(root, 0, True)
        return self.path