class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        for i, num in enumerate(nums + [upper + 1]):
            if num > lower:
                res.append(str(lower))
                if lower != num - 1: res[-1] += "->" + str(num - 1)
            lower = num + 1
        return res
            
