# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        k1 = 0
        p1 = None
        k2 = 0
        p2 = None
        stack = [(root, None, 0)]
        while stack:
            node, p, l = stack.pop()
            if not node:
                continue
            if not p1 and node.val == x:
                p1 = p
                k1 = l
            elif not p2 and node.val == y:
                p2 = p
                k2 = l  
            
            stack.append((node.left, node, l + 1))
            stack.append((node.right, node, l + 1))

        return k1 == k2 and p1.val != p2.val