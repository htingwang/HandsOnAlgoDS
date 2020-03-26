import functools
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        def comp(a, b):
            if a[0] != b[0]: return a[0] - b[0]
            return b[1] - a[1]
        items.sort(key=functools.cmp_to_key(comp))
        #print(items)
        cnt = score = 0
        pre_id = -1
        res = []
        for item in items:
            if item[0] == pre_id: continue
            cnt += 1
            score += item[1]
            if cnt == 5:
                res.append([item[0], score // 5])
                cnt = score = 0
                pre_id = item[0]
        return res
