class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {}
        for i, num in enumerate(nums):
            if target - num in idx:
                return [idx[target - num], i]
            idx[num] = i
        return [-1, -1]
        
