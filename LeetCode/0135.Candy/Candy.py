class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        return self.candy2(ratings)
    
    # One pass. Space: O(1)
    def candy2(self, ratings):
        if not ratings: return 0
        res, cnt, pre = 1, 0, 1
        n = len(ratings)
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                if cnt > 0:
                    res += cnt * (cnt + 1) // 2
                    if cnt >= pre: res += cnt - pre + 1
                    cnt, pre = 0, 1
                pre = 1 if ratings[i] == ratings[i - 1] else pre + 1
                res += pre
            else:
                cnt += 1

        res += cnt * (cnt + 1) / 2
        if cnt >= pre: res += cnt - pre + 1
        return res
        
    # Two pass. Space: O(n)
    def candy1(self, ratings):
        n = len(ratings)
        cnt = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]: cnt[i] = cnt[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: cnt[i] = max(cnt[i], cnt[i + 1] + 1)
        
        return sum(cnt)
