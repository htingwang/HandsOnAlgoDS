class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        ans = 0
        v_l = sorted(zip(values, labels))
        count = collections.defaultdict(int)
        while v_l and num_wanted:
            value, label = v_l.pop()
            if count[label] < use_limit:
                count[label] += 1
                ans += value
                num_wanted -= 1
        return ans
