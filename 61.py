# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length = 2
        tail = head.next
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        
        node = head
        for _ in range(length - k - 1):
            node = node.next

        tail.next = head
        head = node.next
        node.next = None
        return head
        
            
        
