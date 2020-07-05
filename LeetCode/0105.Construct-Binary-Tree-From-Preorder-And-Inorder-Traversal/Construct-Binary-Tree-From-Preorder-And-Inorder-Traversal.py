# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTree2(preorder, inorder)
    
    def buildTree2(self, preorder, inorder):
        
        pre = collections.deque(preorder)
        toidx = {val: i for i, val in enumerate(inorder)}
        n = len(inorder)
        
        def dfs(s, e):
            if s > e: return None
            
            val = pre.popleft()
            root = TreeNode(val)
            root.left = dfs(s, toidx[val] - 1)
            root.right = dfs(toidx[val] + 1, e)
            
            return root
            
        return dfs(0, n - 1)
        
    def buildTree1(self, preorder, inorder):
        if not preorder: return None;
        root = TreeNode(preorder[0]);
        stack = [root];
        i, j = 1, 0;
        while i < len(preorder):
            pop = None;
            while stack and stack[-1].val == inorder[j]:
                pop = stack.pop();
                j += 1;
            node = TreeNode(preorder[i]);
            if pop: 
                pop.right = node;
            else: 
                stack[-1].left = node;
            stack.append(node);
            i += 1;
        return root;
