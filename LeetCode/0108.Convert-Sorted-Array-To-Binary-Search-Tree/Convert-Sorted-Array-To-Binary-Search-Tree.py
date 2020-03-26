# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None

        mid_pos = length // 2
        node = TreeNode(nums[mid_pos])
        if mid_pos == 0:
            return node

        node.left = self.sortedArrayToBST(nums[:mid_pos])
        node.right = self.sortedArrayToBST(nums[mid_pos + 1:])

        return node
