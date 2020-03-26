class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [1] * 5
        
        for i in range(1, n):
            a = count[1] + count[2] + count[4]
            e = count[0] + count[2]
            i = count[1] + count[3]
            o = count[2]
            u = count[2] + count[3]
            count = [a, e, i, o, u]
            
        return sum(count) % (10**9 + 7)
