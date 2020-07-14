class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.majorityElement2(nums)
    
    def majorityElement2(self, nums):
        res = cnt = 0
        for num in nums:
            if cnt == 0: res = num
            if num == res: cnt += 1
            else: cnt -= 1
        return res
        
    def majorityElement1(self, nums):
        nums.sort();
        return(nums[len(nums)/2]);        
