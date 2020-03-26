class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            j = bisect.bisect_left(arr, nums[i])
            res[i] = j
            #if j and j == len(arr) and nums[i] <= arr[-1]: res[i] = 0
            bisect.insort(arr, nums[i])
            #print(nums[i], arr)
        return res
