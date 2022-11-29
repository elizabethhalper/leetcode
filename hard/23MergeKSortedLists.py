# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # TODO: there's also a divide and conquer algo to understand
        # priority queue
#         head = point = ListNode(0)
#         q = queue.PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put((l.val, l))

#         while not q.empty():
#             val = q.get()
#             # point.next is equal to the val we popped off queue
#             point.next = ListNode(val)
#             # make wwhat we just added the point
#             point = point.next
#             # see if the node we took from the queue has a next
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return head.next
        # brute force
        # put all vals into array
        # create new linked list from sorted array
        nodes = []
        merged = None
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
            
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
            
        return head.next