class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = set()
        
        for n in nums:
            sorted_nums.add(n)
            sorted_nums.add(2 * n)
            
        sorted_nums = sorted(sorted_nums)
        rank = {n: i + 1 for i, n in enumerate(sorted_nums)}
        bit = [0] * (len(sorted_nums) + 1)
        
        def update(i, diff):
            while i < len(bit):
                bit[i] += diff
                i += (i & -i)         
                
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= (i & -i)
            return res
        
        res = 0
        for num in reversed(nums):
            res += query(rank[num] - 1)
            update(rank[2 * num], 1)
            
            
        return res
            
