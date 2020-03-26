class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * n
        count = [0] * (n + 1)
        
        for start, end, seats in bookings:
            count[start - 1] += seats
            
            count[end] -= seats
        
        print(count)
        cur = 0
        for i in range(n):
            cur += count[i]
            res[i] = cur
        return res
        
