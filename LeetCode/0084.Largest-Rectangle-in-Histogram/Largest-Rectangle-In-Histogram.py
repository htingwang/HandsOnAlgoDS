class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0;
        stack = [];
        for i in range(len(heights) + 1):
            height = -1
            if i < len(heights): height = heights[i]
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                right = i - 1
                left = stack[-1] if stack else -1
                ans = max(ans, (right - left) * h)
            stack.append(i)
        return ans
