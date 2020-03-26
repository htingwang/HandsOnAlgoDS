class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        correct = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if correct[i] != heights[i]: res += 1
        return res
        
