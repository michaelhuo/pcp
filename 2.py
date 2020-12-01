# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        carry = 0
        head = ListNode(-1)
        node = head
        while head1 and head2:
            value = head1.val + head2.val + carry
            if value > 9:
                value -= 10
                carry = 1
            else:
                carry = 0
            node.next = ListNode(value)
            node = node.next
            head1 = head1.next
            head2 = head2.next
        
        if head2:
            head1 = head2
        
        while head1:
            value = head1.val + carry
            if value > 9:
                value -= 10
                carry = 1
            else:
                carry = 0
            node.next = ListNode(value)
            node = node.next
            head1 = head1.next
        
        if carry:
            node.next = ListNode(carry)
        return head.next
