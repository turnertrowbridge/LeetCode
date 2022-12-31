# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next: # fast moves twice as fast and slow, meaning slow is the middle when fast is at the end
            slow = slow.next
            fast = fast.next.next

        
        return slow