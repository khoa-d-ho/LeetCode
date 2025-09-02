# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        else:
            return []
        
        while queue:
            level = []
            qlen = len(queue)
            for i in range(qlen):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if level:
                if len(res) % 2 != 0:
                    level.reverse()
                res.append(level)

        return res
