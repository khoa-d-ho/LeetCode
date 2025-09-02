# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_len = 0
        stack = [(root, 1)]
        while stack:
            node, l = stack.pop()
            if l > max_len:
                max_len = l
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((node.left, l + 1))
                else:
                    stack.append((node.left, 1))


            if node.right:
                if node.right.val == node.val + 1:
                    stack.append((node.right, l + 1))
                else:
                    stack.append((node.right, 1))

                
        
        return max_len