# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        d = {0:1}
        def dfs(root, prev_sum):
            if not root:
                return

            curr_sum = root.val + prev_sum           
            target = curr_sum - targetSum
            if target in d:
                self.res += d[target]

            if curr_sum in d:
                d[curr_sum] += 1
            else:
                d[curr_sum] = 1


            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            d[curr_sum] -= 1
        
        dfs(root, 0)
        return self.res