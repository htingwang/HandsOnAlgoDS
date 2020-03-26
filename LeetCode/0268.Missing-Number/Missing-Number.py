class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = (1+len(nums))*len(nums)/2;
        for num in nums:
            ans -= num;
        return ans;
        
