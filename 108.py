# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums):
            if not nums:
                return None
            size = len(nums)
            mid = size // 2
            node = TreeNode(nums[mid])
            node.left = helper(nums[0:mid])
            node.right = helper(nums[mid + 1:size])
            return node
        if not nums:
            return None
        root = helper(nums)
        return root
