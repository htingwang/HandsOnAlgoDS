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
    


class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.arr = list(nums)
        self.seg = collections.defaultdict(int)
        self.build(0, n - 1, 0)
        
    def build(self, s, e, idx):
        if s > e: return 0
        if s == e: self.seg[idx] = self.arr[s]
        else:
            mid = (s + e) // 2
            self.seg[idx]= self.build(s, mid, 2 * idx + 1) + self.build(mid + 1, e, 2 * idx + 2)
        return self.seg[idx]

    def _update(self, s, e, i, diff, idx):
        if i > e or i < s: return
        self.seg[idx] += diff
        if s == e: return
        else:
            mid = (s + e) // 2
            self._update(s, mid, i, diff, 2 * idx + 1)
            self._update(mid + 1, e, i, diff, 2 * idx + 2)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._update(0, len(self.arr) - 1, i, val - self.arr[i], 0)
        self.arr[i] = val
        
    def query(self, s, e, i, j, idx):
        if j < s or i > e: return 0
        if i <= s and j >= e: return self.seg[idx]
        mid = (s + e) // 2
        return self.query(s, mid, i, j, 2 * idx + 1) + self.query(mid + 1, e, i, j, 2 * idx + 2)
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(0, len(self.arr) - 1, i, j, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
