class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            _id, rest = log.split(" ", 1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)
