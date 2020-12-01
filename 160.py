# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        node1 = headA
        node2 = headB
        switched1 = switched2 = False
        while node1 and node2:
            if switched1 and switched2:
                if node1 == node2:
                    return node1
            if not node1.next and not switched1:
                switched1 = True
                node1 = headB
            else:
                 node1 = node1.next
            if not node2.next and not switched2:
                switched2 = True
                node2 = headA
            else:
                node2 = node2.next
        return None
