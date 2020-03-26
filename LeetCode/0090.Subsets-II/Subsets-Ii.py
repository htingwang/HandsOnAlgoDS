class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]
        nums.sort()
        last = nums[0]
        last_count = 1
        for num in nums:
            if num != last:
                last = num
                last_count = len(res)
            count = len(res)
            for i in range(count - last_count, count):
                cur = list(res[i])
                cur.append(num)
                res.append(cur)
        return res
