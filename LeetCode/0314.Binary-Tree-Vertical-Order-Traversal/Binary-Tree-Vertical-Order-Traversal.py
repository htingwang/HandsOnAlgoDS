# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = deque()
        queue.append((root, 0, 0))
        res_r = []
        res_l = []
        while queue:
            node, row, col = queue.popleft()
            if col >= 0:
                for _ in range(col - len(res_r) + 1): res_r.append([])
                res_r[col].append(node.val)
            else:
                for _ in range(-col - len(res_l) + 1): res_l.append([])    
                res_l[-col].append(node.val)
            #print(node.val, row, col, res_r, res_l)
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        res = []
        for i in range(len(res_l) - 1, -1, -1):
            if res_l[i] != []: res.append(res_l[i])
        for i in range(len(res_r)):
            if res_r[i] != []: res.append(res_r[i])
        return res
