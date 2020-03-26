class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num != target: continue
            cnt += 1
            if random.randint(1, cnt) == cnt: res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
