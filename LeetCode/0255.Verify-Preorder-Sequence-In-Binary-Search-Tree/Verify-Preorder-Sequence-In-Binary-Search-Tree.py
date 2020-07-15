class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.verifyPreorder1(preorder)
    
    def verifyPreorder2(self, preorder):
        low, i = float('-inf'), -1
        for n in preorder:
            if n < low: return False
            while i >= 0 and n > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = n
        return True
        
    def verifyPreorder1(self, preorder):
        low = float('-inf')
        stack = []
        for n in preorder:
            if n < low: return False
            while stack and n > stack[-1]:
                low = stack.pop()
            stack.append(n)
        return True
