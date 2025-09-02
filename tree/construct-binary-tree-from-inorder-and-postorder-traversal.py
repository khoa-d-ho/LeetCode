# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        

        def help(left, right):
            nonlocal postord_id
            if left > right:
                return None
                
            val = postorder[postord_id]
            root = TreeNode(val)

            postord_id -= 1
            index = index_map[val]
            root.right = help(index + 1, right)
            root.left = help(left, index - 1)

            return root
        index_map = {}
        for i, n in enumerate(inorder):
            index_map[n] = i
        
        postord_id = len(postorder) - 1

        return help(0, len(postorder) - 1)