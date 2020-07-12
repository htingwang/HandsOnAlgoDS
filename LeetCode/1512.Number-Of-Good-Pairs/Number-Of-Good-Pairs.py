class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for num in count:
            if count[num] > 1: 
                res += count[num] * (count[num] - 1) // 2
        
        return res
