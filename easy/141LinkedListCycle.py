# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # hash type
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         ptr = head
#         node_hash = {}
#         while ptr:
#             if ptr in node_hash.keys():
#                 return True
#             else:
#                 node_hash[ptr] = ptr.val
#             ptr = ptr.next
#       return False
    # two pointer type
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow_ptr = head
        fast_ptr = head.next
        while slow_ptr != fast_ptr:
            if fast_ptr is None or fast_ptr.next is None:
                return False
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return True