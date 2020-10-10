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
        
        
        def flattern_dfs(prev: 'Node', curr: 'Node') -> 'Node':
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            next = curr.next
            
            tail = flattern_dfs(curr, curr.child)
            curr.child = None
            tail = flattern_dfs(tail, next)
            return tail
        
        if not head:
            return
        
        pseudo_head = Node(0, None, head, None)
        stack = []
        prev = pseudo_head
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        pseudo_head.next.prev = None
        return pseudo_head.next
    
        #flattern_dfs(pseudo_head, head)
        #pseudo_head.next.prev = None
        return pseudo_head.next
        #recursive(head, None)

        return head
