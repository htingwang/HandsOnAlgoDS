class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #    0
        #  1   2      2^1 - 2 + n
        # 3 4 5 6     2^2 - 2 + n
        
        n = len(nums)
        if n == 1: return nums[0] % 10
        tree = [-1] * 32
        for num in nums:
            d, p, v = num // 100, (num % 100) // 10, num % 10
            tree[2 ** (d - 1) - 2 + p] = v
            
        self.res = 0
            
        def dfs(idx, cur):
            if tree[idx] == -1: return 0
            cur += tree[idx]
            if idx >= 15 or (tree[2 * idx + 1] == -1 and tree[2 * idx + 2] == -1):
                self.res += cur
                return
                
            dfs(2 * idx + 1, cur)
            dfs(2 * idx + 2, cur)
            
        dfs(0, 0)    
            
        return self.res
            

        
