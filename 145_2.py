# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def _postorderTraversal(node: 'TreeNode', output: List[int]) -> None:
            if not node:
                return
            _postorderTraversal(node.left, output)
            _postorderTraversal(node.right, output)
            output.append(node.val)
        
        if not root:
            return root
        output = []
        stack = []
        # visited = set()
        # stack.append(root)
        # while stack:
            # node = stack.pop()
            # output.append(node.val)
            # if node.left:
                # stack.append(node.left)
            # if node.right:
                # stack.append(node.right)
        # _postorderTraversal(root, output)
        node = root
        visited = False
        while node or stack:
            if node:
                if not visited:
                    stack.append((node, False))
                node = node.left
            else:
                node, visited = stack.pop()
                if visited:
                    output.append(node.val)
                else:
                    stack.append((node, True))
                    node = node.right

        # output.reverse()
        return output
        
