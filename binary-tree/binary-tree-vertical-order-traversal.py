# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # system of indices (root = 0)
        # bfs 
        # defaultdict for storing the order (index: node.val)
        # deque to traverse through the nodes in CONST TIME

        if not root:
            return []
        
        res = []
        queue = collections.deque([(0,root)])
        column_index = collections.defaultdict(list)

        max_x = float('-inf')
        min_x = float('inf')

        while queue:
            x, node = queue.popleft()
            column_index[x].append(node.val)

            max_x = max(x, max_x)
            min_x = min(x, min_x)

            if node.left:
                queue.append((x-1, node.left))

            if node.right:
                queue.append((x+1, node.right))

        for level in range(min_x, max_x + 1):
            res.append(column_index[level])

        return res