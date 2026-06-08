# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head        
        temp, prev = None, None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            if not temp:
                head = prev
        
        return head
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head
        length = 0
        while front is not None:
            length += 1
            front = front.next
        
        half_length = length // 2
        front = head

        i = 0
        half_head = None
        prev = None
        while i != half_length:
            prev = front
            front = front.next
            i += 1
        #print(front.val)
        prev.next = None
        
        half_head = self.reverseList(front)
        #print(half_head.val)
        currSecondHalf = half_head
        currFirstHalf = head

        for i in range(length):
            #print(currFirstHalf.val, currSecondHalf.val)
            if not (i % 2):
                temp = currFirstHalf.next
                currFirstHalf.next = currSecondHalf
                currFirstHalf = temp
            else:
                if currFirstHalf is not None:
                    temp = currSecondHalf.next
                    currSecondHalf.next = currFirstHalf
                    currSecondHalf = temp
                else:
                    break
        print(head.val)
        return None           