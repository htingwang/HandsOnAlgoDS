class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exists = [0]*20001;
        for n in nums:
            exists[n+10000] += 1;
        odd = True;
        ret = 0;
        for i in range(20001):
            while (exists[i] > 0):
                if (odd == True):
                    ret += (i-10000);
                exists[i] -= 1;
                odd = not odd;
            
        return ret;
            
        
