class TreeAncestor(object):
    step = 15
    
    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        A = dict(enumerate(parent))
        self.jump = [A]
        for _ in range(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            self.jump.append(B)
            A = B
        

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        step = self.step
        res = node
        while step >= 0:
            while k >= 1 << step:
                if res not in self.jump[step]: return -1
                res = self.jump[step][res]
                k -= 1 << step
            step -= 1
        return res
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
