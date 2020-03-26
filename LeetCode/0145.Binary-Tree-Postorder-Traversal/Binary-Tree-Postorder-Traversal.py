class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        while cur:
            if cur.right:
                pre = cur.right
                while pre.left and pre.left != cur:
                    pre = pre.left
                if pre.left:
                    pre.left = None
                    cur = cur.left
                else:
                    pre.left = cur
                    res.append(cur.val)
                    cur = cur.right
            else:
                res.append(cur.val)
                cur = cur.left
        return res[:: -1]
