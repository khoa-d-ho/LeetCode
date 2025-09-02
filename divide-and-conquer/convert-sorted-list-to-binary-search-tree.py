# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        def array_to_tree(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            left = array_to_tree(left, mid - 1)        

            root = TreeNode(head.val)
            root.left = left
            head = head.next

            root.right = array_to_tree(mid + 1, right) 
            return root
               
        return array_to_tree(0, length - 1)
