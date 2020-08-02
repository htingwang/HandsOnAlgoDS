class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1: return max(arr[0 : 2])
        mx = max(arr)
        cnt = 1
        queue = collections.deque(arr)
        pre = -1
        while cnt < k:
            a, b = queue.popleft(), queue.popleft()
            if b > a: a, b = b, a
            if a == pre: cnt += 1
            else: cnt = 1
            if a == mx: return a
            queue.appendleft(a)
            queue.append(b)
            pre = a
        return pre
