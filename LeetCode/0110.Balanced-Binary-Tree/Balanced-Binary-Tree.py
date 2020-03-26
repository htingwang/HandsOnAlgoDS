# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import namedtuple
class Solution(object):
    def isBalanced(self, tree):
        BalancedStatusWithHeight = namedtuple('xxx', ('balanced', 'height'))
        
        def check_balanced(tree):
            if not tree:
                return BalancedStatusWithHeight(True, -1)
            
            left_result = check_balanced(tree.left)
            if not left_result.balanced:
                return BalancedStatusWithHeight(False, 0)
            
            right_result = check_balanced(tree.right)
            if not right_result.balanced:
                return BalancedStatusWithHeight(False, 0)
            # absolute
            is_balanced = abs(left_result.height - right_result.height) <= 1
            height = max(left_result.height, right_result.height) + 1
            return BalancedStatusWithHeight(is_balanced, height)

        return check_balanced(tree).balanced

