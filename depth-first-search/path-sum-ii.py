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

        stack = [(root, [root.val], root.val)]
        # visited = {root} # only for graphs

        while stack:
            curr_node, curr_path, curr_sum = stack.pop()
            if not curr_node.left and not curr_node.right and curr_sum == targetSum:
                res.append(curr_path)

            if curr_node.right:
                new_path = list(curr_path)
                new_path.append(curr_node.right.val)
                new_sum = curr_sum + curr_node.right.val
                stack.append((curr_node.right, new_path, new_sum))
            if curr_node.left:
                new_path = list(curr_path)
                new_path.append(curr_node.left.val)
                new_sum = curr_sum + curr_node.left.val
                stack.append((curr_node.left, new_path, new_sum))

        return res
            