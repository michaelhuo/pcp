"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def recursive(cur: 'Node', prev: 'Node') -> 'Node':
            #print(cur.val)
            next = cur.next
            child = cur.child
            cur.prev = prev
            last = cur
            
            if child:
                last.child = None
                last.next = child
                last = recursive(child, cur)
                
            if next:
                last.next = next
                last = recursive(next, last)
                
            
                
            return last
        
        if not head:
            return

        recursive(head, None)

        return head
