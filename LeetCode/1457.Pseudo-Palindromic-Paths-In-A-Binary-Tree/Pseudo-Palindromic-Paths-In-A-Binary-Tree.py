# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append((root, {root.val: 1}))
        res = 0
        while queue:
            cur, cnt = queue.popleft()
            for node in [cur.left, cur.right]:
                if node:
                    ncnt = dict(cnt)
                    if node.val in ncnt:
                        ncnt[node.val] -= 1
                        if ncnt[node.val] == 0: del ncnt[node.val]
                    else:
                        ncnt[node.val] = 1
                    queue.append((node, ncnt))
            if not cur.left and not cur.right:
                if len(cnt) == 0 or (len(cnt) == 1 and cnt.values()[0] == 1): res += 1
        return res

        
