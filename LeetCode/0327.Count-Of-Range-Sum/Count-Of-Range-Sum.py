class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # psum = [0, -2, 3, 2]
        # sorted_psum = [-2, 0, 2, 3]
        # psum[j] - psum[i] >= -2, psum[i] <= psum[j] - lower
        # psum[j] - psum[i] <=  2, psum[i] >= psum[j] - upper
        # when psum_j = 2, psum_is = [-2, 0, 3]
        # find 0 <= psum_i <= 4
        
        n = len(nums)
        psum, bit = [0] * (n + 1), [0] * (n + 2)
        
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= (i & -i)
            return res
        
        def update(i, diff):
            while i < len(bit):
                bit[i] += diff
                i += (i & -i)
                
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]
            
        sorted_psum = sorted(psum)
        
        res = 0
        for psum_j in psum:
            cnt_psum_i = query(bisect.bisect_right(sorted_psum, psum_j - lower)) - query(bisect.bisect_left(sorted_psum, psum_j - upper))
            res += cnt_psum_i
            update(bisect.bisect_left(sorted_psum, psum_j) + 1, 1)
            
        return res
                
