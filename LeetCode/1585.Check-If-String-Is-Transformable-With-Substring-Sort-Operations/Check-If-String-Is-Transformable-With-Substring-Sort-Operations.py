class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = collections.defaultdict(list)
        cnt = [0] * 10
        for i, c in enumerate(s):
            idx[ord(c) - ord('0')].append(i)
        
        for c in t:
            num = ord(c) - ord('0')
            if cnt[num] > len(idx[num]) - 1: return False
            for i in range(num):
                if cnt[i] < len(idx[i]) and idx[i][cnt[i]] < idx[num][cnt[num]]:
                    return False
            cnt[num] += 1
            
        return True
        
