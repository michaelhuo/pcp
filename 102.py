# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        curr, next = deque(), deque()
        output = []
        
        node = root
        curr.append(node)
        line = []
        while True:
            if curr:
                node = curr.popleft()
                line.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            else:
                output.append(line)
                line = []
                if next:
                    curr, next = next, curr
                    next.clear()
                else:
                    break
        return output
                    
