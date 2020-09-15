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
        output = []
        stack = []
        dummy = root
        while dummy or stack:
            if dummy:
                stack.append(dummy)
                dummy = dummy.left
            else:
                dummy = stack.pop()
                output.append(dummy.val)
                dummy = dummy.right

        # self._recursive(root, output)
        return output

    def _recursive(self, node: TreeNode, output: List[int]):
        if not node:
            return
        self._recursive(node.left, output)
        output.append(node.val)
        self._recursive(node.right, output)

    
