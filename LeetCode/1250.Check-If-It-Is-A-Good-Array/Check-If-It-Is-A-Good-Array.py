class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def computeGCD(x, y): 
            while(y): 
                x, y = y, x % y 
            return x
        nums = list(set(nums))
        n = len(nums)
        gcd = nums[0]
        for i in range(1, n):
            gcd = computeGCD(gcd, nums[i])
        return gcd == 1
        
