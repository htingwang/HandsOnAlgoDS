class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #return len(set(nums))-len(nums) != 0
        exists = {};
        for num in nums:
            exists[num] = exists.get(num, 0)+1;
            if (exists[num] > 1): return True;
        return False;
