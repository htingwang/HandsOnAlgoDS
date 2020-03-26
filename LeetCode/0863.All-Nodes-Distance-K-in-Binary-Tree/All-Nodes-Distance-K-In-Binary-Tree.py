class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        self.dfs(root, target, K, ans)
        return ans
    
    def dfs(self, node, target, K, ans):
        if not node:
            return -1
        if node == target:
            self.subtree(target, 0, K, ans)
            return 1
        
        L, R = self.dfs(node.left, target, K, ans), self.dfs(node.right, target, K, ans)
        if L != -1:
            if L == K:
                ans.append(node.val)
            self.subtree(node.right, L + 1, K, ans) 
            return L + 1
        elif R != -1:
            if R == K:
                ans.append(node.val)
            self.subtree(node.left, R + 1, K, ans)
            return R + 1
        else:
            return -1
        
    def subtree(self, node, dist, K, ans):
        #if node: print(node.val)
        if not node or dist > K:
            return 
        if dist == K:
            ans.append(node.val)
        else:
            self.subtree(node.left, dist + 1, K, ans)
            self.subtree(node.right, dist + 1, K, ans)
