# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        dummy = ListNode
        node = dummy
        while l1 or l2:
            if not l1:
                node.next = l2
                l2 = l2.next
                node = node.next
            elif not l2:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                    node = node.next
                else:
                    node.next= l2
                    l2 = l2.next
                    node = node.next
        return dummy.next
