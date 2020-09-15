# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        output = []
        stack = []
        #self._recursive(root, output)
        stack.append(root)
        while stack:
            dummy = stack.pop()
            output.append(dummy.val)
            if dummy.right:
                stack.append(dummy.right)
            if dummy.left:
                stack.append(dummy.left)

        return output

    def _recursive(self, root: TreeNode, output: List[int]):
        if not root:
            return
        output.append(root.val)
        self._recursive(root.left, output)
        self._recursive(root.right, output)
        
