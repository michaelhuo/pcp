# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head
        prev = None
        while node.next:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        node.next = prev
        return node
