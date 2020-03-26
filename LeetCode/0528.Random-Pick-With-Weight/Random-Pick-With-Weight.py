class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = list(w)
        for i in range(1, len(w)):
            self.prefix[i] = self.prefix[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        # [1,     2,         5]
        # [1,     3,         8]
        # [0,   1,2, 3,4,5,6,7]
        target = random.randint(0, self.prefix[-1] - 1)
        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = left + (right - left) // 2
            #print(mid)
            if self.prefix[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
