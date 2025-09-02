# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.next_items = []
        self.max_depth = 0
    def nextMaxDepth(self):
        if not self.next_items:
            return self.max_depth

        next_node, next_level = self.next_items.pop(0)
        next_level += 1
        self.max_depth = max(self.max_depth, next_level)
        if next_node.left:
            self.next_items.append((next_node.left, next_level))
        if next_node.right:
            self.next_items.append((next_node.right, next_level))
        
        return self.nextMaxDepth()
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.next_items = [(root, 0)]
        self.max_depth = 0

        return self.nextMaxDepth()

        