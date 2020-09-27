class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        cost = 0
        res = -1
        left = 0
        cur = 0
        run = 1
        for i, c in enumerate(customers):
            left += c
            cur += min(left, 4)
            left -= min(left, 4)
            if cur * boardingCost - run * runningCost > cost:
                res = run
                cost = cur * boardingCost - run * runningCost
            #print(cur, run, cost, left)
            run += 1
        
        while left > 0:
            
            cur += min(left, 4)
            left -= 4
            if cur * boardingCost - run * runningCost > cost:
                res = run
                cost = cur * boardingCost - run * runningCost
            #print(run,cost)
            run += 1
            
        return res
        #10,10,1,0,0
        #1: 4*4-4*1=12
        #2: 4*8-4*2=24
        #3: 4*12-4*3=36
        #4: 4*16-4*4=48
        #5: 4*20-4*5=60
        #6: 4*21-4*6=60
