# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def recursive(root: TreeNode, nums:List[int]) -> None:
            if root.left:
                recursive(root.left, nums)
            nums.append(root.val)
            if root.right:
                recursive(root.right, nums)
        nums = []
        recursive(root, nums)
        low, high = 0, len(nums) - 1
        while low < high:
            value = nums[low] + nums[high]
            if value == k:
                return True
            elif value < k:
                low += 1
            else:
                high -= 1
        return False
            
