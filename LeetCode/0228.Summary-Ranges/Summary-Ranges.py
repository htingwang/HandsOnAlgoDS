class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = []
        s = e = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or nums[i + 1] - num > 1:
                e = i
                if s != e: res.append(str(nums[s]) + "->" + str(nums[e]))
                else: res.append(str(nums[s]))
                s = e = i + 1
        return res
        
