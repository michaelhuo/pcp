# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        size = len(preorder)
        
        inorder_indices = {v:i for i, v in enumerate(inorder)}
        def helper(in_left: int, in_right: int) -> TreeNode:
            nonlocal preorder_index
            if in_left == in_right:
                return None
            root_value = preorder[preorder_index]
            index = inorder_indices[root_value]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)
            return root
        preorder_index = 0
        return helper(0, size)
