class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = collections.deque([("0000", 0)])
        seen = set(deadends)
        if "0000" in seen: return -1
        seen.add("0000")
        #print(seen)
        while queue:
            cur, dist = queue.popleft()
            #print(cur, dist)
            if cur == target: return dist
            for i, c in enumerate(cur):
                n = 0 if int(c) == 9 else int(c) + 1
                p = 9 if int(c) == 0 else int(c) - 1
                if cur[: i] + str(n) + cur[i + 1 : ] not in seen:
                    seen.add(cur[: i] + str(n) + cur[i + 1 : ])
                    queue.append((cur[: i] + str(n) + cur[i + 1 : ], dist + 1))
                if cur[: i] + str(p) + cur[i + 1 : ] not in seen:
                    seen.add(cur[: i] + str(p) + cur[i + 1 : ])
                    queue.append((cur[: i] + str(p) + cur[i + 1 : ], dist + 1))
        return -1
