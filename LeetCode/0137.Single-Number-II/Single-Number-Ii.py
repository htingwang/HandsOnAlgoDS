class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = twice = 0
        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)
        return once
