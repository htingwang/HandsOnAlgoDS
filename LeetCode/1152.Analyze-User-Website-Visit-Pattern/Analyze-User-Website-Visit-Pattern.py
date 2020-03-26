class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        by_user = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)
        #print(by_user)
        cnt = collections.Counter()
        for x in by_user.values():
            #print(x)
            cnt += collections.Counter(set(itertools.combinations(x, 3)))
        #print(cnt)
        return min(cnt, key=lambda k: (-cnt[k], k))
