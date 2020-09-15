# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [(root, False)]
        node, visited = (root, False)

        #self._recursive(root, result)
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                result.append(node.val)

        return result

    def _recursive(self, root: TreeNode, result: List[int]):
        if not root:
            return
        self._recursive(root.left, result)
        self._recursive(root.right, result)
        result.append(root.val)
         
