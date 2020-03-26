class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        save = maxsave= 0
        for i in range(len(customers)):
            if not grumpy[i]: res += customers[i]
            if grumpy[i]: save += customers[i]
            if i >= X - 1:
                if i >= X and grumpy[i - X]: save -= customers[i - X]
                #print(i, save)
                maxsave = max(maxsave, save)
        #print(res)
        return res + maxsave
        
