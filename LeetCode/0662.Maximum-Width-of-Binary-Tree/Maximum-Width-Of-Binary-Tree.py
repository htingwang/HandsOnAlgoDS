# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        queue = collections.deque([(root, 1)])
        while queue:
            size = len(queue)
            left = right = 0
            for i in range(size):
                cur, idx = queue.popleft()
                if i == 0: left = idx
                if i == size - 1: right = idx
                if cur.left: queue.append((cur.left, idx * 2))
                if cur.right: queue.append((cur.right, idx * 2 + 1))
            res = max(res, right - left + 1)
        return res
