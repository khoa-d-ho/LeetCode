# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def help(left, right):
            nonlocal preord_index
            if left > right:
                return None
            val = preorder[preord_index]
            root = TreeNode(val = val)
            preord_index += 1
            index = index_map[val]

            root.left = help(left, index-1)
            root.right = help(index + 1, right)
            return root
        index_map = {}
        for i, e in enumerate(inorder):
            index_map[e] = i

        preord_index = 0
        root = help(0, len(preorder) - 1)
        return root