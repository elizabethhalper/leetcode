# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's Nodes
# (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1)
        # keep track of ret value
        dummy.next = head
        prev = dummy
        while head and head.next:
            #set nodes to be swapped
            n1 = head
            n2 = head.next
            # run swap on pair
            prev.next = n2
            n1.next = n2.next
            n2.next = n1
            # set up for next iteration
            prev = n1
            head = n1.next
        
        return dummy.next