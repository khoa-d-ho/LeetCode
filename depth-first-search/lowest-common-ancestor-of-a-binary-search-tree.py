# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # recursion
        # recurse to the subtree which has both p and q
        # return curr_node if 
            # p and q in diff subtrees
            # OR either p or q is curr_node
        # DFS

        # in order traversal gives flattened sorted tree
        # move left if p and q < root
        # move right if p and q > root
        # if p or q == root:
            # return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

        '''
        p = 2
        q = 8
        '''