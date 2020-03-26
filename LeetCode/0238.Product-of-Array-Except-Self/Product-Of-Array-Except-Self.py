class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1];
        for i in range(1, len(nums)):
            ans.append(nums[i-1]*ans[i-1]);
        prod = 1;
        for i in range(len(nums)-2,-1,-1):
            prod *= nums[i+1];
            ans[i] *= prod;        
        return ans;
        
