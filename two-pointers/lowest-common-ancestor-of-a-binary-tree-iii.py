"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # store path from p to root
        # go from q to root, first same point with path is LCA
        path = []
        while p:
            path.append(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q
        