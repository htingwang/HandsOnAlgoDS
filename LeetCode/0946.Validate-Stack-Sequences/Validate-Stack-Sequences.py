class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        n = len(pushed)
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == n
        
