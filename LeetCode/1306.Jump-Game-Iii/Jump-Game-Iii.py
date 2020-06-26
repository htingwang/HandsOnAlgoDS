class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        return self.canReach2(arr, start)
    
    def canReach2(self, arr, start):
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = - arr[start]
            return arr[start] == 0 or self.canReach2(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False
        
    def canReach1(self, arr, start):
        n = len(arr)
        seen = [False] * n
        queue = collections.deque([start])
        seen[start] = True
        while queue:
            cur = queue.popleft()
            if arr[cur] == 0: return True
            l, r = cur - arr[cur], cur + arr[cur]
            for i in [l, r]:
                if 0 <= i < n and seen[i] == False:
                    queue.append(i)
                    seen[i] = True
        return False
