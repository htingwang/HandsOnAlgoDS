class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums: diff ^= num
        diff &= -diff # find right most 1 (the first bit difference of two single numbers)
        res = [0, 0]
        for num in nums:
            if num & diff: res[0] ^= num
            else: res[1] ^= num
        return res
        
