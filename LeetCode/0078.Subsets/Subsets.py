class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        tmp = [];
        def backtrace(ans, tmp, nums, start):
            ans.append(list(tmp));
            for i in range(start, len(nums)):
                tmp.append(nums[i]);
                backtrace(ans, tmp, nums, i+1);
                tmp.pop();
            
            
        backtrace(ans, tmp, nums, 0);
        
        return ans;
            
        
