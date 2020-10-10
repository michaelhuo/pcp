# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def _isValidBST(root: TreeNode) -> (bool, int, int):

            root_val = root.val
            is_valid = True
            left_min_val = root_val
            left_max_val = root_val
            if root.left:
                is_valid, left_min_val, left_max_val = _isValidBST(root.left)
                if not is_valid:
                    return (False, 0, 0)
                left_min_val = min(left_min_val, root_val)

                if left_max_val >= root_val:
                    return (False, left_min_val, left_max_val)
                else:
                    left_max_val = root_val
            right_min_val = root_val
            right_max_val = root_val
            if root.right:
                is_valid, right_min_val, right_max_val = _isValidBST(root.right)
                if not is_valid:
                    return (False, 0, 0)

                right_max_val = max(right_max_val, root_val)
                if right_min_val <= root_val:
                    return (False, 0, 0)
                else:
                    right_min_val = root_val
            
            return (True, left_min_val, right_max_val)
        
        if not root:
            return True
        
        (is_valid, _, _) = _isValidBST(root)
        return is_valid

