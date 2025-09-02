# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, goodN, maxVal):
        if not root:
            return 
        
        if root.left:
            if root.left.val >= maxVal:
                goodN.append(root.left.val)
                self.helper(root.left, goodN, root.left.val)
            else:
                self.helper(root.left, goodN, maxVal)
        
        if root.right:
            if root.right.val >= maxVal:
                goodN.append(root.right.val)
                self.helper(root.right, goodN, root.right.val)
            else:
                self.helper(root.right, goodN, maxVal)
 

    def goodNodes(self, root: TreeNode) -> int:
        nodes = [root.val]
        self.helper(root, nodes, maxVal = root.val)
        return len(nodes)