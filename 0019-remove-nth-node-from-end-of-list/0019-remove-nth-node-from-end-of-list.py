# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):          # move fast n nodes ahead of slow
            fast = fast.next
        
        if not fast:                # if fast is None due to the nth value being out of bounds
            return head.next

        while fast.next:            # move nodes to next until fast hits end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # delete the nth value
        return head