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
        preorder_indices = {v:i for i, v in enumerate(preorder)}
        inorder_indices = {v:i for i, v in enumerate(inorder)}

        def build_subtree(inorder_low: int, inorder_high: int) -> TreeNode:
            root_preorder_index = size
            for i in range(inorder_low, inorder_high):
                idx = preorder_indices[inorder[i]]
                if idx < root_preorder_index:
                    root_preorder_index = idx
                    
            root_val = preorder[root_preorder_index]
            root_index = inorder_indices[root_val]
            root = TreeNode(root_val)
            if root_index > inorder_low:
                root.left = build_subtree(inorder_low, root_index)
            if root_index + 1 < inorder_high:
                root.right = build_subtree(root_index + 1, inorder_high)
            return root
        node = build_subtree(0, size)
        return node
