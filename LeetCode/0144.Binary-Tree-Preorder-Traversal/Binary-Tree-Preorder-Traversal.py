class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if pre.right:
                    pre.right = None
                    cur = cur.right
                else:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right
        return res
