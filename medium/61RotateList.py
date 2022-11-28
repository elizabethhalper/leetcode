# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateList(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        count = 0         
        
        # loop through linked list and find tail
        while start.next != None:
            start = start.next
        
        # Add loop
        start.next = head
        #find new tail
        new_tail = head
        while count < k:
            count += 1
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # set new tail's next to null
        new_tail.next = None

        return new_head