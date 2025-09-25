# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        # visited = {root} # only for graphs

        
        def backtrack(curr_node, curr_path, curr_sum):
            if not curr_node.left and not curr_node.right:
                if curr_sum == targetSum:
                    res.append(curr_path[:])

            if curr_node.left:
                curr_path.append(curr_node.left.val)
                backtrack(curr_node.left, curr_path, curr_sum + curr_node.left.val)
                curr_path.pop()
            if curr_node.right:
                next_path = curr_path.append(curr_node.right.val)
                backtrack(curr_node.right, curr_path, curr_sum + curr_node.right.val)
                curr_path.pop()

        backtrack(root, [root.val], root.val)
        return res