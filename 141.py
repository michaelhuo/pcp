# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = p2 = head
        if not head:
            return False
        while p2:
            if not p2.next:
                return False
            p1 = p1.next
            p2 = p2.next.next
            # print("p1={},p2={}".format(p1.val, p2.val))
            if p1 == p2:
                return True
        return False
            