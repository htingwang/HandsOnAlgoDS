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
