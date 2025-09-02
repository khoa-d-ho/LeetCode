# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # empty tree
        if not root: 
            return []
        # analyse first level: root
        queue = deque([root])
        res = [] # store result

        while queue: # stop when nothing else to process
            # at the start, all nodes of that level is in queue
            curr_level_size = len(queue) 
            # only loop through those values
            for i in range(curr_level_size):
                curr = queue.popleft() # analyse
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # add last item of each level to result
                if i == curr_level_size -1:
                    res.append(curr.val)
        return res

            