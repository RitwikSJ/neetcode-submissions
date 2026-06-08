# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        curr1 = list1
        curr2 = list2
        head = None

        if (curr1.val < curr2.val):
            head = list1
            curr1 = curr1.next
        else:
            head = list2
            curr2 = curr2.next
        
        prev = head

        while curr1 is not None and curr2 is not None:
            if (curr1.val < curr2.val):
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        
        if curr1 is None:
            prev.next = curr2
        else:
            prev.next = curr1
        
        return head
        