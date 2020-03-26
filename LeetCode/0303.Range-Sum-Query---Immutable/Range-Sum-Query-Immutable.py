class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.s = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.s[i] = self.s[i - 1] + nums[i - 1]
        #print self.s

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j + 1] - self.s[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
