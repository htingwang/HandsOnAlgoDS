class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i in range(len(height)):
            #print(i, stack)
            while stack and height[stack[-1]] < height[i]:
                pop = stack.pop()
                if stack:
                    top = stack[-1]
                    w = i - top -1
                    h = min(height[i], height[top]) - height[pop]
                    #print(w, h)
                    res += w * h
                    #print res
            stack.append(i)
        return res    
