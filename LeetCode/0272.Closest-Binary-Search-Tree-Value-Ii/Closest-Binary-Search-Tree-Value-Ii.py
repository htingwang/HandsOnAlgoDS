# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = collections.deque()
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            cur = stack.pop()
            if len(res) < k:
                res.append(cur.val)
            else:
                if abs(target - cur.val) < abs(target - res[0]):
                    res.popleft()
                    res.append(cur.val)
                else: break
            node = cur.right
        return list(res)
        
