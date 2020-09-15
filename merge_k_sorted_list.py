import heapq
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1 and not lists[0]:
            return None
        head = ListNode(-1)
        tail = head
        hq = []
        for l in lists:
            while l:
                heappush(hq, l.val)
                l = l.next
        while hq:
            node = ListNode(heappop(hq))
            tail.next = node
            tail = tail.next

        head = head.next
        return head
