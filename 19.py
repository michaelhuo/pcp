# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = tail = head
        
        for _ in range(n):
            tail = tail.next
        if not tail:
            return head.next
        while tail.next:
            prev = prev.next
            tail = tail.next
        prev.next = prev.next.next
        return head
        
