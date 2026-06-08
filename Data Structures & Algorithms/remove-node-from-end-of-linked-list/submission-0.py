# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        removedNode = head
        prev = None

        while removedNode != None:
            length += 1
            removedNode = removedNode.next
        
        removedNode = head
        prev = None
        i = 0
        removedIndex = length - n
        print(length, removedNode, removedIndex)

        while i != removedIndex:
            prev = removedNode
            removedNode = removedNode.next
            i += 1
        
        if prev:
            prev.next = removedNode.next
        else:
            head = removedNode.next
        return head
        