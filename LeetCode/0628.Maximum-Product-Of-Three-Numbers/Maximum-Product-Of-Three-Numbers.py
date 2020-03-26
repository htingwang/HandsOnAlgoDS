class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1, min2 = 1001, 1001;
        max1, max2, max3 = -1001, -1001, -1001;
        for num in nums:
            if num >= max3:
                max1 = max2;
                max2 = max3;
                max3 = num;
            elif num >= max2:
                max1 = max2;
                max2 = num;
            elif num >= max1:
                max1 = num;
            if num <= min1:
                min2 = min1;
                min1 = num;
            elif num <= min2:
                min2 = num;
        return max(min1*min2*max3, max1*max2*max3);
        
