# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def _isValidBST(root: TreeNode) -> (bool, int, int):
            if not root:
                return (True, None, None)
            root_val = root.val
            left_valid, left_min, left_max = _isValidBST(root.left)
            if not left_valid:
                return (False, None, None)
            if left_min is None:
                left_min = root_val
                
            if left_max is None:
                left_max = root_val
            else:
                if left_max >= root_val:
                    return (False, None, None)
                else:
                    left_max = root_val
            right_valid, right_min, right_max = _isValidBST(root.right)
            if not right_valid:
                return (False, None, None)
            if right_min is None:
                right_min = root_val
            else:
                if right_min <= root_val:
                    return (False, None, None)
                else:
                    right_min = root_val
            if right_max is None:
                right_max = root_val
                
            return (True, left_min, right_max)
        
        if not root:
            return True
        
        (is_valid, left_val, right_val) = _isValidBST(root)
        return is_valid

