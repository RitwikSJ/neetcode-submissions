# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        prev = None
        new = None
        head = None

        while cur1 or cur2:
            curVal = 0
            if cur1:
                curVal += cur1.val
            if cur2:
                curVal += cur2.val

            if curVal > 9:
                new = ListNode(curVal % 10)
                if cur1 and cur1.next:
                    cur1.next.val += 1
                elif cur2 and cur2.next:
                    cur2.next.val += 1
                else:
                    additionalNode = ListNode(1)
                    new.next = additionalNode
            else:
                new = ListNode(curVal)

            print(prev.val if prev else None, new.val if new else None, head.val if head else None)

            if prev:
                prev.next = new
            else:
                head = new
            prev = new

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
                
        return head
        