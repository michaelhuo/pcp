# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def _inorderTraversal(node: TreeNode, output: List[int]) -> None:
            if not node:
                return
            _inorderTraversal(node.left, output)
            output.append(node.val)
            _inorderTraversal(node.right, output)
        
        if not root:
            return root
        stack = []
        output = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            if stack:
                node = stack.pop()
                output.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = None
                        
                
        # _inorderTraversal(root, output)
        return output
        
