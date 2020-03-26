# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        if (not S): return None;
        stack = [];
        endidx = S.find("-")
        if (endidx == -1): endidx = len(S)
        root = TreeNode(S[0:endidx]);
        stack.append(root);
        level,prelevel = 0,0;
        idx = endidx;
        node = root;
        while (idx < len(S)):
            if S[idx] == '-':
                level += 1;
                idx += 1;
            else:
                endidx = S[idx:].find("-");  
                if (endidx == -1): endidx = len(S)
                newnode = TreeNode(S[idx:idx+endidx]);
                #print("newnode:"+str(S[idx:idx+endidx])+" size "+str(len(stack)))
                #print("level "+str(level)+" "+str(prelevel))
                idx += endidx;
                if (level > prelevel):
                    node.left = newnode;
                    #print(str(node.val)+" left is "+(newnode.val))
                    stack.append(newnode);
                else:
                    for i in range(prelevel-level+2):
                        node = stack.pop();
                    #print len(stack);
                    #print("level "+str(level)+" "+str(prelevel))
                    #print(prelevel-level+2)
                    node.right = newnode;
                    #print(str(node.val)+" right is "+(newnode.val))
                    stack.append(node);
                    stack.append(newnode);
                #print("append:"+str(newnode.val)+" size "+str(len(stack)))
                #print("level "+str(level)+" "+str(prelevel))
                node = newnode;
                prelevel = level;
                level = 0;
            
        return root;
