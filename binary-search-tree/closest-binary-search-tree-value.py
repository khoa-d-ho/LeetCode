# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_val = root.val  # Initialize the closest value as the root's value

        while root:
            # Update the closest value if the current value is closer
            if abs(root.val - target) < abs(min_val - target):
                min_val = root.val
            elif abs(root.val - target) == abs(min_val - target):
                min_val = min(min_val, root.val)
            # Traverse the tree
            if root.val < target:
                root = root.right
            else:  # root.val >= target
                root = root.left
        
        return min_val

'''
Time Complexity
O(H): H is the height of the BST.
In a balanced tree, H = log N.
In a skewed tree, H = N.

Space Complexity
O(1):
'''