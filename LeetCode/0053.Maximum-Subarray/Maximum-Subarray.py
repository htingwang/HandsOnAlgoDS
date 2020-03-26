class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsum = ans = nums[0];
        for i in range(1, len(nums)):
            if subsum < 0: subsum=0;
            subsum += nums[i];
            ans = max(ans, subsum);
        return ans;
            
        
