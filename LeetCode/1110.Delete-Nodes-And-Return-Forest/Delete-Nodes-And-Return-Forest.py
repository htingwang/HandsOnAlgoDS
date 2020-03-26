class Solution(object):
    def delNodes(self, root, to_delete):
        res = []
        self.dfs(root, True, set(to_delete), res)
        return res
    def dfs(self, node, is_prev_del, to_del_set, res):
        if is_prev_del == True and node.val not in to_del_set:
            res.append(node)
        if node.left:
            self.dfs(node.left, node.val in to_del_set, to_del_set, res)
            if node.left.val in to_del_set:
                node.left = None
        if node.right:
            self.dfs(node.right, node.val in to_del_set, to_del_set, res)
            if node.right.val in to_del_set:
                node.right = None

