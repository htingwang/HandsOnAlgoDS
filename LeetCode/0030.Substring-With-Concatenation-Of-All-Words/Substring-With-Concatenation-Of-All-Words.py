class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        n = len(s)
        size = len(words[0])
        count = collections.Counter(words)
        wordmap = {}
        res = []
        for i in range(len(s) - size + 1):
            if s[i: i + size] in count:
                wordmap[i] = s[i: i + size]
        for i in range(size):
            cur = dict(count)
            check = 0
            # j * size + i < n, j < (n - i) / size
            left = -1
            for j in range((n - i) // size + 1):
                right = j * size + i
                #print(left, right, check, cur)
                if right in wordmap:
                    if left == -1: left = right
                    cur[wordmap[right]] -= 1
                    if cur[wordmap[right]] == 0:
                        check += 1
                        if check == len(count): 
                            res.append(left)
                    if (right - left) == size * (len(words) - 1) and left in wordmap:
                        cur[wordmap[left]] += 1
                        if cur[wordmap[left]] > 0: check -= 1
                        left += size
                else:
                    cur = dict(count)
                    check = 0
                    left = -1      
        return res
        
