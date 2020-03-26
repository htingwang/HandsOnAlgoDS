class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def dfs(count):
            ans = 0
            for key in range(len(count)):
                if not count[key]: continue
                ans += 1
                count[key] -= 1
                ans += dfs(count)
                count[key] += 1
            return ans
        #count = collections.Counter(tiles)
        count = [0] * 26
        for c in tiles:
            count[ord(c) - ord("A")] += 1
        #print count
        return dfs(count)
        
