class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.BITree = [0] * (len(nums) + 1)
        self.nums = [0] * len(nums)

        for i, num in enumerate(nums):
            self.update(i, num)
        
        #print(self.nums)
        #print(self.BITree)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        #print(i, delta)
        i += 1
        while i < len(self.BITree):
            #print(i, val)
            self.BITree[i] += delta
            #print(self.BITree)
            i += (i & -i)
        #print(self.BITree)
        
    def query(self, i):   
        res = 0
        #print(i)
        while i > 0:
            res += self.BITree[i]
            i -= (i & -i)
        #print(i, res,self.BITree)
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(j + 1) - self.query(i)
    
