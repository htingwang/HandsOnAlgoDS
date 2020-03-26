class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [sys.maxsize]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                cur = stack.pop()
                res += cur * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
