# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            curr_level = []
            for i in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                curr_level.append(curr_node.val)
            res.append(curr_level)
        return res