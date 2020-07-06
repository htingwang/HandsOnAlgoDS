# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbers2(root)
   
    # Morris traversal. Space: O(1)
    def sumNumbers2(self, root):
        res = cur = 0
        node = root
        while node:
            if node.left:
                pre = node.left
                step = 1
                while pre.right and pre.right != node: 
                    pre = pre.right
                    step += 1
                if pre.right:
                    if not pre.left: res += cur
                    for _ in range(step): cur //= 10
                    pre.right = None
                    node = node.right
                else:
                    cur = cur * 10 + node.val
                    pre.right = node
                    node = node.left
            else:
                cur = cur * 10 + node.val
                if not node.right: res += cur
                node = node.right
                
        return res
        
    def sumNumbers1(self, root):
        self.res = 0
        def dfs(node, cur):
            if not node: return
            cur = cur * 10 + node.val
            if not node.left and not node.right: self.res += cur
            dfs(node.left, cur)
            dfs(node.right, cur)
            
        dfs(root, 0)
        return self.res
