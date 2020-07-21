class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def func(x, a, b, c):
            return a * x *x + b * x + c
        
        n = len(nums)
        res = collections.deque()
        left, right = 0, n - 1
        while left <= right:
            if a >= 0:
                if func(nums[left], a, b, c) > func(nums[right], a, b, c):
                    res.appendleft(func(nums[left], a, b, c))
                    left += 1
                else:
                    res.appendleft(func(nums[right], a, b, c))
                    right -= 1
            else:
                if func(nums[left], a, b, c) < func(nums[right], a, b, c):
                    res.append(func(nums[left], a, b, c))
                    left += 1
                else:
                    res.append(func(nums[right], a, b, c))
                    right -= 1
        return list(res)
