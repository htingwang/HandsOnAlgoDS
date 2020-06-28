class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        p = [1] * n
        for i in range(1, n):
            p[i] = (p[i - 1] * 2) % mod
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += p[j - i] % mod
                i += 1
        return res % mod
