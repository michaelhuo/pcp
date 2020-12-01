"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_level(root: 'Node', parent:'Node' = None, is_left: bool = True) -> None:
            if not parent:
                root.next = None
            else:
                if is_left:
                    root.next = parent.right
                else:
                    if parent.next:
                        root.next = parent.next.left
            if root.right:
                connect_level(root.right, root, False)
            if root.left:
                connect_level(root.left, root, True)
        if not root:
            return None
        connect_level(root)
        return root
