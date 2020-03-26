class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1] * len(nums)
        
        for i, num in enumerate(nums + nums):
            #print(i, stack)
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            #if res[-1] != -1: break
            stack.append(i % len(nums))
        return res
        
        
