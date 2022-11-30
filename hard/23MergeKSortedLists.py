# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

import queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
#         nodes = []
#         merged = None
#         head = point = ListNode(0)
#         for l in lists:
#             while l:
#                 nodes.append(l.val)
#                 l = l.next
            
#         for x in sorted(nodes):
#             point.next = ListNode(x)
#             point = point.next
            
#         return head.next

        # divide and conquer
        num_lists = len(lists)
        interval = 1
        # start with each list right next to each other merging
        while interval < num_lists:
            for i in range(0, num_lists-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
                # because we merged lists, the interval btw lists to merge doubles
            interval *= 2
        return lists[0] if num_lists > 0 else None
            
    def merge2Lists(self, list_1, list_2):
        # made up node so wwe have something to start with
        head = point = ListNode(0)
        while list_1 and list_2:
            if list_1.val <= list_2.val:
                point.next = list_1
                # put the first node in list one next
                list_1 = list_1.next
            else:
                # the first one in list 2 is smaller so that list is next
                point.next = list_2
                # make list 2 list 1
                list_2 = list_1
                # list 1 is now the remainder of list 2 (why do we have to do this?)
                list_1 = point.next.next
            point = point.next
        if not list_1:
            point.next = list_2
        else:
            point.next = list_1
        # return after made-up node
        print(head.next)
        return head.next