class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (2 * n)
        for i in range(n):
            res[2 * i] = nums[i]
            res[2 * i + 1] = nums[i + n]
        return res
        
