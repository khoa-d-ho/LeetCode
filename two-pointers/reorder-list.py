# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle of linked list
        slow, fast = head, head.next
        while fast and fast.next: # two valid nodes
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None # cut 1st half from 2nd half

        # reverse 2nd half of list
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
            
        # in the end prev will be the new head
        head2 = prev

        while head and head2:
            temp1, temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head = temp1 
            head2 = temp2


        