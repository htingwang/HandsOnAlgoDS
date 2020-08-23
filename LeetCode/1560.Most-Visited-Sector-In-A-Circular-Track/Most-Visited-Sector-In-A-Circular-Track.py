class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        s = rounds[0]
        r = [s, s]
        count = 0
        for i in range(1, len(rounds)):
            cur, prev = rounds[i], rounds[i - 1]
            count += cur - prev
            if cur <= prev: count += n
        count = count % n + 1
        #print(count)
        res = []
        if s + count - 1 > n:
            res = list(range(1, s + count - 1 - n + 1)) + list(range(s, n + 1))
        else: res = list(range(s, s + count))
        return res
                    
