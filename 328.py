# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        head_even = head.next 
        head_odd = head
        tail_even = head_even
        tail_odd = head_odd
        is_odd = True
        node = head.next.next
        while node:
            if is_odd:
                tail_odd.next = node
                tail_odd = tail_odd.next
            else:
                tail_even.next = node
                tail_even = tail_even.next
            is_odd = not is_odd
            node = node.next
        tail_even.next = None
        tail_odd.next = head_even
        return head
        
            
