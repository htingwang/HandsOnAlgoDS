class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        return self.canCompleteCircuit2(gas, cost)
    
    def canCompleteCircuit2(self, gas, cost):
        total = cur = res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                res = i + 1
                cur = 0
        return res if total >= 0 else -1
                
        
    def canCompleteCircuit1(self, gas, cost):
        #    -2, -2, -2, (3, 3, -2, -2, -2), 3, 3
        # 0, -2, -4, -6, -3, 0, -2, -4, -6, -3, 0
        # minimun sliding window
        # monotone increasing stack
        n = len(gas)
        pre = [0] * 2 * n
        for i in range(2 * n - 1):
            pre[i + 1] = pre[i] + gas[i % n] - cost[i % n]
        queue = collections.deque()
        for i in range(1, 2 * n):
            while queue and pre[queue[-1]] > pre[i]: queue.pop()
            queue.append(i)
            if i >= n:
                if pre[queue[0]] >= pre[i - n]:
                    return i - n
                if queue[0] == i - n + 1: queue.popleft()
        return -1

        
