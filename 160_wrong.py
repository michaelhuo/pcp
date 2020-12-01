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
        same = False
        value = 0
        same_node = None
        while node1 and node2:
            if switched1 and switched2:
                if node1.val == node2.val:
                    if not same:
                        same = True
                        value = node1.val
                        same_node = node1
                else:
                    if same:
                        same = False
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
            
        if same:
            return same_node
        else:
            return None
