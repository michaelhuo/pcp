# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        
        length  = 0
        node = head
        while node:
            length += 1
            node = node.next
        length2 = 0
        if length % 2 == 0:
            length2 = length // 2
            is_even = True
            mid = length2
        else:
            length2 = length // 2
            is_even = False
            mid = length2 + 1
        node = head
        for _ in range(length2):
            node = node.next
        head2 = node
        if not is_even:
            head2 = head2.next
        node_mid = head2.next

        node = head2
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        tail = prev
        result = True
        head1 = head
        head2 = tail
        while head2:
            if head1.val != head2.val:
                result = False
                break
            head1 = head1.next
            head2 = head2.next
        prev = None
        node = tail
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return result
            
        
