class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max3exist = 0;
        max1 = max2 = max3 = -sys.maxsize-1;
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2;
                max2 = max1;
                max1 = nums[i];
                max3exist += 1;
            elif nums[i] > max2:
                if (nums[i] != max1):
                    max3 = max2;
                    max2 = nums[i];
                    max3exist += 1;
            elif nums[i] > max3:
                if (nums[i] != max2):
                    max3 = nums[i];
                    max3exist += 1;
        #print [max3exist,max1,max2,max3]
        if max3exist >= 3:
            return max3;
        else:
            return max(max1, max2, max3);
        
