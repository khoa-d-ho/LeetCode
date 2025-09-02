# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        current = 0
        if not head:
            return 0

        slow = head
        fast = head
        elements = []
        while fast and slow:
            elements.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        for i in elements[::-1]:
            current = i + slow.val
            if current > max_sum: 
                max_sum = current

            slow = slow.next
        return max_sum