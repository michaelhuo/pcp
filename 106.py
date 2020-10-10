# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def _buildTree(inorder: List[int], postorder: List[int]) -> 'TreeNode':
            if not inorder or not postorder or len(inorder) != len(postorder):
                return None
            if len(inorder) == 1:
                if inorder[0] == postorder[0]:
                    node = TreeNode(inorder[0])
                    return node
                else:
                    return None
            
            root_val = postorder[-1]
            root_index = inorder.index(root_val)
            root = TreeNode(root_val)
            if root_index == 0:
                right = _buildTree(inorder[1:], postorder[:-1])
                root.right = right
            elif root_index == len(inorder) - 1:
                left = _buildTree(inorder[:-1], postorder[:-1])
                root.left = left
            else:
                left_list = inorder[:root_index]
                right_list = inorder[root_index + 1:]
                left = _buildTree(left_list, [i for i in postorder if i in left_list])
                right = _buildTree(right_list, [i for i in postorder if i in right_list])
                root.left = left
                root.right = right
            return root
        
        return _buildTree(inorder, postorder)
