# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
clarification: 
- binary tree balanced? anything
- 2 <= n <= 10^5
- any two nodes with same val? no!

'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursion
        # recurse to the subtree which has both p and q
        # return curr_node if 
            # p and q in diff subtrees
            # OR either p or q is curr_node

        if not root or root == q or root == p:
            return root
        
        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)

        if left_subtree and right_subtree:
            return root
        
        return left_subtree if left_subtree else right_subtree
