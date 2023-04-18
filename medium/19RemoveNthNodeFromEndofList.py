# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        dummy = ListNode(-1)
        dummy.next = head
        while ptr != None:
            count+=1
            ptr = ptr.next
        num_to_remove = count - n

        count = 0
        ptr = dummy

        while count < num_to_remove:
            count+=1
            ptr = ptr.next
        
        # if ptr.next:
        ptr.next = ptr.next.next

        return dummy.next