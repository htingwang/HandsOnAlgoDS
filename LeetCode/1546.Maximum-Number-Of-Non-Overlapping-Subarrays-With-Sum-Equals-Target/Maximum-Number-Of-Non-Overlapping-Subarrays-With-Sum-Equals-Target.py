class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        pre_set = set([0])
        res = 0
        for i in range(1, n + 1):
            #print(pre[i], pre_set)
            if pre[i] - target in pre_set:
                res += 1
                pre_set = set([pre[i]])
            else:
                pre_set.add(pre[i])
        return res
