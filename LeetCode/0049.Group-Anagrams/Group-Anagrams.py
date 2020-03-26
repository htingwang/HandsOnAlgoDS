class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = collections.defaultdict(list)
        for s in strs:
            group[tuple(sorted(s))].append(s)
        return group.values()
