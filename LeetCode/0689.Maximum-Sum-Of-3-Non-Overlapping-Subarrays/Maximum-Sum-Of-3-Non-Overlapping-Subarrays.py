class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        pre = [0] * (n + 1)
        left, right = [0] * n, [n - k] * n
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        total = pre[k] - pre[0] 
        for i in range(k, n):
            if (pre[i + 1] - pre[i + 1 - k] > total):
                left[i] = i + 1 - k
                total = pre[i + 1] - pre[i + 1 - k]
            else:
                left[i] = left[i - 1]
        total = pre[n] - pre[n - k] # n-k ~ n-1
        for i in range(n - 1 - k, -1, -1):
            if (pre[i + k] - pre[i] >= total):
                right[i] = i
                total = pre[i + k] - pre[i]
            else:
                right[i] = right[i + 1]

        sum_3 = float('-inf')
        for i in range(k, n - 2 * k + 1):
            l, r = left[i - 1], right[i + k]
            total = (pre[i + k] - pre[i]) + (pre[l + k] - pre[l]) + (pre[r + k] - pre[r])
            if (total > sum_3):
                sum_3 = total
                res = [l, i, r]
        return res

