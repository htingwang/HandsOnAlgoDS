class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = last = res = 0
        for i in range(len(nums) - 1):
            cur = max(cur, i + nums[i])
            if i == last:
                res += 1
                last = cur
                if cur >= len(nums) - 1: break
        return res
        
