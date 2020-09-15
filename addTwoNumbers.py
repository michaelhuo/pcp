#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head, current = None, None
        while (l1 or l2):
            value1, value2, value = 0, 0, 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next

            value = value1 + value2 + carry
            node = ListNode(value % 10)

            if current:
                current.next = node
                current = current.next
            else:
                current = node
                head = current

            carry = 1 if value > 9 else 0

        if carry:
            node = ListNode(1)
            current.next = node

        return head

if __name__ == "__main__":
    list = ListNode(9)
    list.next = ListNode(4)
    print(Solution().addTwoNumbers(list, ListNode(1)).myPrint())
