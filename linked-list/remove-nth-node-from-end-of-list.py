# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        before = dummy
        after = dummy
        dummy.next = head
        for i in range(n):
            after = after.next
        if not after.next:
            return head.next
        else:
            while after.next:
                after = after.next
                before = before.next
            if head == before.next:
                return before.next
            before.next = before.next.next
            return head
        
