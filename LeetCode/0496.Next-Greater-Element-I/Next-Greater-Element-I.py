class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}
        res = []
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            if num in next_greater:
                res.append(next_greater[num])
            else:
                res.append(-1)
        return res
        
