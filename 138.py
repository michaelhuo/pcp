"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        mapping = {}
        node = head
        node_copied = Node(node.val)
        head_copied = node_copied
        mapping[node] = node_copied
        prev = node_copied
        while node.next:
            node = node.next
            node_copied = Node(node.val)
            prev.next = node_copied
            mapping[node] = node_copied
            prev = node_copied
        node = head
        node_copied = head_copied
        while node:
            if node.random:
                node_copied.random = mapping[node.random]
            else:
                node_copied.random = None
            node = node.next
            node_copied = node_copied.next
        return head_copied
    
