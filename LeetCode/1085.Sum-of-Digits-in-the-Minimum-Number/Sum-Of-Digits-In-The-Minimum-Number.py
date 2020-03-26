class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        x = str(min(A))
        tmp = 0
        for i in x:
            tmp += int(i)
        #print(tmp, int(tmp % 2 == 0))
        return int(tmp % 2 == 0)
        
