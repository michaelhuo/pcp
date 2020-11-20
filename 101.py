from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            values = []
            count = 0
            for _ in range(size):
                node = queue.popleft()
                if node:
                    values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    count += 1
                else:
                    values.append(None)
            if count == 0:
                break

            for i in range(size // 2):
                if values[i] != values[size - i - 1]:
                    return False
        return True
