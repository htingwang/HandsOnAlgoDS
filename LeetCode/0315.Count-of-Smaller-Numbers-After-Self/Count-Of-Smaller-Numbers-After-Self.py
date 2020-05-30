class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.countSmaller1(nums)
    
    # Binary index tree. Time: O(NlogN)
    def countSmaller1(self, nums):
        rank = {num: i + 1 for i, num in enumerate(sorted(nums))} 
        n = len(nums)
        bit = [0] * (n + 1)
        
        def update(i, val):
            while i < len(bit):
                bit[i] += val
                i += (i & -i)
                
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= (i & -i)
            return res
                
        res = []
        for num in reversed(nums):
            res.append(query(rank[num] - 1))
            update(rank[num], 1)
            
        return res[::-1]
    
    # Binary Search. Time: O(N^2) because insort takes O(N)
    def countSmaller2(self, nums):
        arr = []
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            j = bisect.bisect_left(arr, nums[i])
            res[i] = j
            #if j and j == len(arr) and nums[i] <= arr[-1]: res[i] = 0
            bisect.insort(arr, nums[i])
            #print(nums[i], arr)
        return res
