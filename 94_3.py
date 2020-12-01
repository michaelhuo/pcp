# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = []
        node = root
        answer = []
        while queue or node:
            if not node:
                node = queue.pop()
                answer.append(node.val)
                node = node.right
            else:
                queue.append(node)
                node = node.left
                
        return answer
