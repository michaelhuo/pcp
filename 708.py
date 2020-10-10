"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head == head.next:
            node = Node(insertVal, head)
            head.next = node
            return head
        
        curr = head
        was_greater = insertVal > curr.val
        
        while True:
            prev = curr
            curr = curr.next
            #print(curr.val)
            if curr.val < prev.val:
                if insertVal > prev.val or insertVal < curr.val:
                    node = Node(insertVal, curr)
                    prev.next = node
                    return head
                was_greater = True
                continue
                
            if was_greater:
                if insertVal <= curr.val:
                    node = Node(insertVal, curr)
                    prev.next = node
                    return head

            was_greater = insertVal > curr.val
            
            if curr == head:
                node = Node(insertVal, curr)
                prev.next = node
                return head               
        return head

