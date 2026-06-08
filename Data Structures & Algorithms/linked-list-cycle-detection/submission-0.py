# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        while slow is not None and fast is not None:
            if slow.val == fast.val:
                return True
            
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
        
        return False
        